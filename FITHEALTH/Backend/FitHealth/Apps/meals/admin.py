from django.contrib import admin
from Apps.meals.models import Meal, MealPlan, MealPlanItem

# Register your models here.

admin.site.register(Meal)
admin.site.register(MealPlan)
admin.site.register(MealPlanItem)