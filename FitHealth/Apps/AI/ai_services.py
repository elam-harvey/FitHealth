from django.conf import settings
from google import genai
from google.genai import types
from Apps.workouts.models import WorkoutPlan, WorkoutPlanItem
from Apps.meals.models import Meal, MealPlan, MealPlanItem
from Apps.users.models import UserProfile

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
        exersices: A list of dictionaries representing individual exersices.
        meals: A list of dictionaries representing individual meals.
        each dict MUST contain the following keys:
            -name: The name of the exersice or meal
            -details: For exersices, this should include sets, reps, and rest time. For meals, this should include calories, protein, carbs, and fats.
    """

    try:
        if not exersices and not meals:
            return "Failed to save plans: No exersices or meals provided."
        
        # create a new plan for the user
        new_workout_plan = WorkoutPlan.objects.create(user=user, name=plan_name)  
        new_meal_plan = MealPlan.objects.create(user=user, name=plan_name)

        # save exersices to the workout plan
        for ex in exersices:
            workout_item = WorkoutPlanItem.objects.create(
                workout_plan=new_workout_plan,
                exercise_name=ex['name'],
                sets=ex['details']['sets'],
                reps=ex['details']['reps'],
                rest_time=ex['details']['rest_time']
            )

        # save meals to the meal plan
        for meal in meals:
            meal_item = MealPlanItem.objects.create(
                meal_plan=new_meal_plan,
                meal_name=meal['name'],
                calories=meal['details']['calories'],
                protein=meal['details']['protein'],
                carbs=meal['details']['carbs'],
                fats=meal['details']['fats']
            )
        return "Plans saved successfully."
    except Exception as e:
        print(f"Error saving plans: {e}")
        return "Failed to save plans due to an error."
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

        # 2.existing Workout Plan logic
        active_plan = WorkoutPlan.objects.filter(user=user).first()
        workout_text = "No active workout plan found."
        if active_plan:
            workout_text = f"Active workout plan: {active_plan.name}, Duration: {active_plan.duration} weeks."
            for item in active_plan.items.all():
                workout_text += f" Exercise: {item.exercise.name}, Sets: {item.sets}, Reps: {item.reps}. "

        # 3. existing Meal Plan logic
        meal_plan = MealPlan.objects.filter(user=user).first()
        meal_text = "No active meal plan found."
        if meal_plan:
            meal_text = f"Active meal plan: {meal_plan.name}, Duration: {meal_plan.duration} weeks."
            for item in meal_plan.items.all():
                meal_text += f" Meal: {item.meal.name}, Calories: {item.meal.calories}, Protein: {item.meal.protein}g, Carbs: {item.meal.carbs}g, Fats: {item.meal.fats}g. "

        # 4. Combine EVERYTHING into a single layout for Gemini
        context_block = f"""
        USER PHYSICAL METRICS & HEALTH PROFILE:
        {profile_text}

        CURRENT WORKOUT PLAN:
        {workout_text}

        CURRENT MEAL PLAN:
        {meal_text}
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
                """Create and save the generated workout plans and meal plans"""
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
                    # Route 1 handle profile modification
                    if call.name == "ai_profile_updater":
                        result = ai_profile_updater(**call.arguments)
                        print(f"Profile update result: {result}")
                    # Route 2 handle plan creation
                    elif call.name == "ai_plan_creator":
                        result = ai_plan_creator(**call.arguments)
                        print(f"Plan creation result: {result}")
                    else:
                        continue

                    # feed the results back to gemini for a user-facing response
                    follow_up_response = self.client.models.generate_content(
                        model=self.model_name,
                        contents=[
                            types.Content(role="user", parts=[types.Part.from_text(text=user_input)]),
                            response.candidates[0].content,
                            types.Content(role="user", parts=[types.Part.from_text(text=f"Tool execution result: {result}")])
                        ])
                    return follow_up_response.text
                
            return response.text
        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"Error generating coaching response: {e}")
            return "Sorry, I'm having trouble generating a response right now. Please try again later."