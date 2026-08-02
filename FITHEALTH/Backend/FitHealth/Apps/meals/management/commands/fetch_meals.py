import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from Apps.meals.models import Meal
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()

# A command to fetch meal data from an external API and populate the database
class Command(BaseCommand):
    help = 'Fetches meal data from an external API and populates the database.'
    
    def add_arguments(self, parser):
        parser.add_argument('--query', type=str, default='Edamame quinoa', help='The keyword to search for recipes')


    def handle(self, *args, **options):
        search_query = options['query']

        # Fetch meal data from the external API
        app_id = os.getenv('EDAMAM_APP_ID')
        app_key = os.getenv('EDAMAM_APP_KEY')
        url = url = f"https://api.edamam.com/api/recipes/v2"

        params = {
            "type": "public",    
            "q": search_query,
            "app_id": app_id,
            "app_key": app_key
        }

        saved_meals = 0
        total_meals = 0

        try:
            response = requests.get(url, params=params)

            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f'Error fetching meal data: {response.status_code}'))
                return
            
            # Parse the JSON response
            data = response.json()
            hits = data.get('hits', [])

            # Create a new Meal object for each hit
            for hit in hits:
                recipe = hit['recipe']
                
                # get the uri instead of the id for edamam
                uri = recipe.get('uri', '')
                id = uri.split('_')[-1] if '_' in uri else uri

                name = recipe.get('label', '')
                image = recipe.get('image', '')

                # since they dont have a description i used the diet labels as a description
                diet_labels = recipe.get('dietLabels', [])
                description = ', '.join(diet_labels) if diet_labels else 'No description available'
                
                # Create a new Meal object
                meal, created = Meal.objects.update_or_create(
                    id=id,
                    defaults={
                        'name': name,
                        'description': description
                    }
                    
                )
                self.stdout.write(self.style.SUCCESS(f'Created meal: {meal.name}'))

                if image and (created or not meal.image):
                    try:
                        # fetch the image bytes (added a timeout to avoid hanging)
                        img_response = requests.get(image, timeout=5)

                        if img_response.status_code == 200:
                            #create a clean file name
                            img_filename = f'meal_{id}.jpg'
                            # This actually upload the image to cloudinary and save the url to the meal object
                            meal.image.save(img_filename, ContentFile(img_response.content), save=True)
                            self.stdout.write(self.style.SUCCESS(f'Saved image to cloudinary: {img_filename}'))
                        else:
                            self.stdout.write(self.style.ERROR(f'Error saving image: {img_response.status_code}'))
                    except requests.RequestException as e:
                        self.stdout.write(self.style.ERROR(f'Error fetching image: {e}'))

                if created:
                    saved_meals += 1
                total_meals += 1

            self.stdout.write(self.style.SUCCESS(f'Total meals saved: {saved_meals}'))
            self.stdout.write(self.style.SUCCESS(f'Total meals fetched: {total_meals}'))
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching meal data: {e}'))

