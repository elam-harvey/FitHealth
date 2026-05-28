from rest_framework import serializers
from .models import Workout, WorkoutPlan, WorkoutPlanItem


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class WorkoutPlanSerializer(serializers.ModelSerializer):
    workouts = WorkoutSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'workouts']

class WorkoutPlanItemSerializer(serializers.ModelSerializer):
    workout = WorkoutSerializer(read_only=True)

    class Meta:
        model = WorkoutPlanItem
        fields = ['id', 'workout', 'day_of_week', 'time_of_day']