from django.core.management.base import BaseCommand
from FITHEALTH.Backend.FitHealth.Apps.workouts.models import Workout

class Command(BaseCommand):
    """Command to populate the database with sample workout data."""
    help = 'Populates the database with sample workout data for testing and development purposes.'
    
    def handle(self, *args, **options):
        # Sample workout data
        workouts_data = [
            {
                "name": "Morning Cardio",
                "description": "A quick cardio session to start your day.",
                "duration": 30,
                "calories_burned": 250,
                "category": "Cardio",
                "importance": "Cardio workouts are essential for improving cardiovascular health, increasing endurance, and burning calories, which can help with weight management and overall fitness.",
            },
            {
                "name": "Strength Training",
                "description": "Build muscle with this strength training routine.",
                "duration": 45,
                "calories_burned": 400,
                "category": "Strength",
                "importance": "Helps build muscle mass and improve overall strength, which is essential for maintaining a healthy metabolism and preventing injuries.",
            },
            {
                "name": "Yoga Flow",
                "description": "A relaxing yoga flow to improve flexibility.",
                "duration": 60,
                "calories_burned": 200,
                "category": "Flexibility",
                "importance": "Trains the body and mind, improving flexibility and reducing stress.",
            },
        ]

        count = 0

        for workout_data in workouts_data:
            workout, created = Workout.objects.get_or_create(**workout_data)
            if created:
                count += 1
                self.stdout.write(self.style.SUCCESS(f'Created workout: {workout.name}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with sample workouts. {count} new workouts added.'))