from django.contrib import admin
from Apps.workouts.models import Workout, WorkoutPlan, WorkoutPlanItem

admin.site.register(Workout)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutPlanItem)
