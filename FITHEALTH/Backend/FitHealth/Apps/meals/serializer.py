from rest_framework import serializers
from .models import Meal, MealPlan, MealPlanItem


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class MealPlanSerializer(serializers.ModelSerializer):
    meals=MealSerializer(many=True, read_only=True)
    class Meta:
        model = MealPlan
        fields = '__all__'

class MealPlanItemSerializer(serializers.ModelSerializer):
    meal = MealSerializer(read_only=True)
    class Meta:
        model = MealPlanItem
        fields = '__all__'