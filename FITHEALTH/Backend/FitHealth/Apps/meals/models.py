from django.db import models


class Meal(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    image = models.ImageField(max_length=2000, upload_to='meal_images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    category = models.CharField(blank=True, null=True)
    importance = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.description}"

# stores the meal plans created for users, and the meals that are part of those plans. 
class MealPlan(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='meal_plans', null=True, blank=True)
    name = models.CharField(max_length=255)
    meals = models.ManyToManyField(Meal, related_name='meal_plans')

    def __str__(self):
        return self.name
    
# Maps Meals to Meal Plans
class MealPlanItem(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='items')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    time_of_day = models.CharField(max_length=20, choices=MEAL_TYPES)

    def __str__(self):
        return f"{self.meal_plan.name} - {self.meal.name} on {self.day_of_week} at {self.time_of_day}"