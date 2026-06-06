from django.conf import settings
from google import genai
from google.genai import types
from FITHEALTH.Backend.FitHealth.Apps.workouts.models import Workout, WorkoutPlan, WorkoutPlanItem
from FITHEALTH.Backend.FitHealth.Apps.meals.models import Meal, MealPlan, MealPlanItem
from FITHEALTH.Backend.FitHealth.Apps.users.models import UserProfile

def update_user_profile_metrics(user, current_weight:float=None, target_weight:float=None, goal: str=None) -> str:
    """Update the user's profile with the latest information so as to be able to tweak the plans"""
    try:
        profile = UserProfile.objects.get(user=user)
        if current_weight is not None:
            profile.current_weight = current_weight
        if target_weight is not None:
            profile.target_weight = target_weight
        if goal is not None:
            profile.goal = goal
        profile.save()
        return "Profile updated successfully."
    except Exception as e:
        print(f"Error updating profile: {e}")
        return "Failed to update profile due to an error."

def save_generated_plans(user, plan_name: str, exersices: list[dict], meals: list[dict]):
    """
    Create and save the generated workout plans and meal plans

    Args:
        plan_name: A descriptive title for the plan, e.g. "John's 4-Week Weight Loss Plan"
        exersices: A list of dictionaries representing individual exercises.
        meals: A list of dictionaries representing individual meals.
    """
    try:
        if not exersices and not meals:
            return "Failed to save plans: No exercises or meals provided."
        
        # 1. Create top-level plan containers
        new_workout_plan = WorkoutPlan.objects.create(user=user, name=plan_name)  
        new_meal_plan = MealPlan.objects.create(user=user, name=plan_name)

        # 2. Securely loop through exercises, using .get() to avoid KeyErrors and providing defaults where necessary
        saved_exersices = 0
        for item in exersices:
            workout_id = item.get('workout_id')
            day = item.get('day', 'monday').lower()  # Default to Monday if not provided
            time = item.get('time', 'morning').lower()  # Default to Morning if not provided
                
            try:
            # direct database lookup to ensure referential integrity
                workout_instance = Workout.objects.get(id=workout_id)

                # link the existing catalog row straight to the user's customized schedule line
                WorkoutPlanItem.objects.create(
                    workout_plan=new_workout_plan,
                    workout=workout_instance,
                    day_of_week=day,
                    time_of_day=time
                )
                saved_exersices += 1
            except Workout.DoesNotExist:
                print(f"Workout with ID {workout_id} does not exist. Skipping this exercise.")
                continue
             
            
        # 3. Save meals cleanly
        for meal in meals:
            m_name = meal.get('name') or meal.get('meal_name')
            if not m_name:
                continue
                
            # Safely check nested 'details' block, fall back to flat item dictionary if missing
            details = meal.get('details', meal)

            meal_instance, created = Meal.objects.get_or_create(
                name=m_name.title(),
                defaults={
                    'calories': details.get('calories', 0),
                    'description': details.get('description', 'AI Generated Meal')
                }
            )

            try:
                MealPlanItem.objects.create(
                    meal_plan=new_meal_plan,
                    meal=meal_instance,
                    
                )
            except Exception as item_error:
                print(f"Skipped adding {m_name} to plan due to model mismatch: {item_error}")
                continue
            
        return "Plans saved successfully."
        
    except Exception as e:
        print(f"Error saving plans: {e}")
        return f"Failed to save plans due to an error: {str(e)}"
class GeminiCoachService:
    def __init__(self):
        """Initialize the Gemini Coach Service with the API key from settings."""
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model_name = "gemini-3.5-flash"  # Use the latest Gemini  

    def receive_user_data(self, user) -> str:
        """Receive user information and store it for personalized coaching"""
    
    # 1. NEW: Fetch the core physical profile metrics
        try:
            profile = UserProfile.objects.get(user=user)
            profile_text = (
                f"Goal: {profile.goal or 'Not set'}\n"
                f"Current Weight: {profile.current_weight}kg | Target Weight: {profile.target_weight}kg\n"
                f"Height: {profile.height}cm | Age: {profile.age} | Gender: {profile.gender}\n"
                f"Activity Level: {profile.activity_level or 'Not set'}\n"
                f"Medical Conditions: {profile.medical_conditions or 'None'}"
            )
        except Exception:
            profile_text = "No profile information filled out yet."

        # fetch alll the available workout from the api and store it in the db
        available_workouts = Workout.objects.all().values('id', 'name', 'category', 'difficulty', 'equipment', 'target_muscle')
        workout_library_text= ""
        for workout in available_workouts:
            workout_library_text += f"ID: {workout['id']}, Name: {workout['name']}, Category: {workout['category']}, Difficulty: {workout['difficulty']}, Target: {workout['target_muscle']}, Equipment: {workout['equipment']}\n"
        if not workout_library_text:
            workout_library_text = "No workouts available in the library."

        # 3. existing Meal Plan logic
        meal_library_text = ""
        available_meals = Meal.objects.all().values('id', 'name', 'calories')
        for meal in available_meals:
            meal_library_text += f"ID: {meal['id']}, Name: {meal['name']}, Calories: {meal['calories']}\n"
        if not meal_library_text:
            meal_library_text = "No meals available in the library."
        # 4. Combine EVERYTHING into a single layout for Gemini
        context_block = f"""
        USER PHYSICAL METRICS & HEALTH PROFILE:
        {profile_text}

        CURRENT WORKOUT PLAN:
        {workout_library_text}

        CURRENT MEAL PLAN:
        {meal_library_text}
        """
        return context_block
        
    def generate_coaching_response(self, user,  user_input: str) -> str:
        """Generate a coaching response based on user data"""

        db_context = self.receive_user_data(user)

        try:
            # Tool A: Profile Metric modifier wrapper

            def ai_profile_updater(current_weight:float=None, target_weight:float=None, goal: str=None)-> str:
                """Update the profile with the latest user information so as to be able to tweak the plans"""
                return update_user_profile_metrics(user, current_weight, target_weight, goal)

            # Tool B: NEW Plan creation tool
            def ai_plan_creator(plan_name: str, exersices: list[dict], meals: list[dict]) -> str:
                """
                Create and save the generated workout plans and meal plans

                Args:
                    plan_name: Title of the plan.
                    exercises: A list of dicts tracking exercises. Each dict MUST look like:
                               {'workout_id': int, 'day': 'monday'/'tuesday'/etc, 'time': 'morning'/'afternoon'/'evening'}
                               Choose the 'workout_id' exclusively from the numbers in the context block!
                    meals: A list of dicts containing nutrition targets.
                            Each dict MUST look like:
                            {'name': str}
                """
                return save_generated_plans(user, plan_name, exersices, meals)
            
            # define the operational settings bundle
            response = self.client.models.generate_content(
                model = self.model_name,
                contents = user_input,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "You are a FITHEALTH AI Personal coach. You are an expert "
                        "a Nutritionist, Personal Trainer, and Wellness Coach. You provide personalized advice "
                        f"CRITICAL CURRENT USER DATABASE CONTEXT:\n{db_context}\n\n"
                        "RULES:\n"
                        "based on the user's health data, fitness goals, and preferences. "
                        "You are empathetic, supportive, and motivational. You help users stay on track with their fitness journey, offering practical tips and encouragement. "
                        "You can provide workout recommendations, nutrition advice, and wellness tips. You are always positive and focused on helping the user achieve their goals. "
                        "Use the user's data to provide personalized and actionable advice. Always encourage the user and celebrate their progress. " \
                        "Make sure to ask follow-up questions to better understand the user's needs and preferences. "
                        "Be consice and direct in your responses, while still being supportive and encouraging. "
                    ),
                    tools = [ai_profile_updater, ai_plan_creator],
                    temperature=0.5,
                )
            )

            # Automatic Tool Execution Parser loop
            if response.function_calls:
                for call in response.function_calls:
                    if call.name == 'ai_profile_updater':
                        tool_result = ai_profile_updater(**call.args)
                    
                    elif call.name == 'ai_plan_creator':
                        tool_result = ai_plan_creator(**call.args)
                    else:
                        continue

                    #  Send a clean, streamlined payload for the final recap
                    follow_up_response = self.client.models.generate_content(
                        model=self.model_name,
                        contents=f"The system has executed the requested tool function. Result: {tool_result}. Summarize this for the user conversationally and confirm it has been saved to their profile database.",
                        config=types.GenerateContentConfig(
                            system_instruction="You are the FITHEALTH AI Coach. Confirm database changes concisely and encouragingly.",
                            temperature=0.3
                        )
                    )
                    return follow_up_response.text

            return response.text
        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"Error generating coaching response: {e}")
            return "Sorry, I'm having trouble generating a response right now. Please try again later."