from django.core.management.base import BaseCommand
from FITHEALTH.Backend.FitHealth.Apps.meals.models import Meal


class Command(BaseCommand):
    """Command to populte the database with sample meal data."""
    help = 'Populates the database with sample meals'

    def handle(self, *args, **options):
        # Sample meal data
        meals_data = [
            {
                "name": "Grilled Chicken Salad",
                "description": "A healthy salad with grilled chicken, mixed greens, and a light vinaigrette.",
                "calories": 350,
                "category": "Lunch",
                "importance": "A balanced meal that provides lean protein and essential nutrients, making it ideal for weight management and overall health.",
            },
            {
                "name": "Oatmeal with Berries",
                "description": "Warm oatmeal topped with fresh berries and a drizzle of honey.",
                "calories": 250,
                "category": "Breakfast",
                "importance": "A nutritious breakfast option that is high in fiber and antioxidants, helping to keep you full and energized throughout the morning.",
            },
            {
                "name": "Quinoa and Veggie Stir-Fry",
                "description": "A colorful stir-fry with quinoa, mixed vegetables, and a savory sauce.",
                "calories": 400,
                "category": "Dinner",
                "importance": "A nutrient-dense meal that provides a good balance of carbohydrates, protein, and vitamins, supporting muscle recovery and overall wellness.",
            },
        ]

        count = 0

        for meal_data in meals_data:
            meal, created = Meal.objects.get_or_create(**meal_data)
            if created:
                count += 1
                self.stdout.write(self.style.SUCCESS(f'Created meal: {meal.name}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with sample meals. {count} new meals added.'))