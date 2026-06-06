import requests
from django.core.management.base import BaseCommand
from FITHEALTH.Backend.FitHealth.Apps.workouts.models import Workout
from django.conf import settings


# Command to fetch workout data from an external API and populate the database
class Command(BaseCommand):
    help = 'Fetches workout data from an external API and populates the database.'

    def handle(self, *args, **options):
        api_url = "https://exercisedb.p.rapidapi.com/exercises"

        offset = 0
        limit = 100
        total_count = 0 # Track total across all pages

        while True:
            #  Use the dynamic variables, not hardcoded strings!
            querystring = {
                "limit": str(limit),  
                "offset": str(offset),
                "sortOrder": "ascending",
                "sortMethod": "bodyPart"
            } 
            
            headers = {
                "X-RapidAPI-Key": settings.RAPID_API_KEY, # Make sure this matches your settings.py spelling!
                "X-RapidAPI-Host": "exercisedb.p.rapidapi.com",
                "Content-Type": "application/json"
            }

            try:
                response = requests.get(api_url, headers=headers, params=querystring)
                print(f"Fetching offset {offset}... Status: {response.status_code}")
                response.raise_for_status()  
                
                workouts_data = response.json()  
                
                # 🛠️ FIX 2: Break the infinite loop if the API returns an empty list
                if not workouts_data:
                    self.stdout.write(self.style.SUCCESS('Reached the end of the API data!'))
                    break

                page_count = 0
                for workout_data in workouts_data:
                    external_id = str(workout_data.get('id', '')) 
                    if not external_id:
                        continue  
                    
                    raw_instructions = workout_data.get('instructions', [])
                    instructions_text = " ".join(raw_instructions)

                    raw_secondary_muscles = workout_data.get('secondaryMuscles', [])
                    secondary_muscles_text = ", ".join(raw_secondary_muscles)
                    
                    detailed_description = (
                        f"Category: {workout_data.get('category', 'N/A')}\n"
                        f"Body Part: {workout_data.get('bodyPart', 'N/A')}\n"
                        f"Target Muscle: {workout_data.get('target', 'N/A')}\n"
                        f"Secondary Muscles: {secondary_muscles_text}\n"
                        f"Equipment: {workout_data.get('equipment', 'N/A')}\n"
                        f"Instructions: {instructions_text}"
                    )
                    
                    workout, created = Workout.objects.get_or_create(
                        api_source_id=external_id,
                        defaults={
                            'name': workout_data.get('name', 'Unknown').title(),
                            'duration': 30, # Defaulting to 30 mins
                            'category': workout_data.get('bodyPart', 'General').title(),
                            'difficulty': workout_data.get('difficulty', 'Medium').title(),
                            'target_muscle': workout_data.get('target', 'N/A'),
                            'secondary_muscle': workout_data.get('secondaryMuscles', 'N/A')
                        }
                    )
                    if created:
                        page_count += 1
                        total_count += 1
                
                self.stdout.write(self.style.SUCCESS(f'Page complete. Added {page_count} new workouts.'))
                
                # Increase the offset for the next loop iteration
                offset += limit
                
            except requests.RequestException as e:
                self.stdout.write(self.style.ERROR(f'Error fetching data from API: {e}'))
                break # Exit the loop if the API crashes

        self.stdout.write(self.style.SUCCESS(f'Sync completely finished! {total_count} total new workouts added.'))