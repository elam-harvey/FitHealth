from .models import Motivation, Snack, Exercises, ActiveChallenge
from rest_framework import serializers
from Apps.workouts.serializer import WorkoutPlanItemSerializer, WorkoutPlanSerializer
from Apps.meals.serializer import MealPlanItemSerializer, MealPlanSerializer

class MotivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivation
        fields = '__all__'

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = '__all__'

class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = '__all__'

class ActiveChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveChallenge
        fields = '__all__'

class DashboardSerializer(serializers.Serializer):
    # data from other modules 
    workouts = WorkoutPlanSerializer(many=True)
    meals = MealPlanSerializer(many=True)

    # data from this module
    motivation = MotivationSerializer()
    snacks = SnackSerializer(many=True)
    exercises = serializers.SerializerMethodField()
    active_challenges = ActiveChallengeSerializer(many=True)

    user = serializers.DictField()

    def get_exercises(self, obj):
        return [exercise.name for exercise in obj['exercises']]