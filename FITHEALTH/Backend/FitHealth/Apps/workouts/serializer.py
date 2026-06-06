from rest_framework import serializers
from .models import Workout, WorkoutPlan, WorkoutPlanItem


# 1. The bottom layer (You already have this built!)
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__' 

# 2. The middle layer (The Linker)
class WorkoutPlanItemSerializer(serializers.ModelSerializer):
    # This nests the full RapidAPI exercise details inside the schedule item!
    workout = WorkoutSerializer(read_only=True)

    class Meta:
        model = WorkoutPlanItem
        fields = ['id', 'workout', 'day_of_week', 'time_of_day']

# 3. The top layer (The Parent Container)
class WorkoutPlanSerializer(serializers.ModelSerializer):
    workouts = WorkoutPlanItemSerializer(source='items', many=True, read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'workouts']