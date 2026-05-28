from django.shortcuts import render
from rest_framework import viewsets
from Apps.meals.permissions import IsPremiumOrReadOnly
from .models import Meal, MealPlan, MealPlanItem
from .serializer import MealSerializer, MealPlanSerializer, MealPlanItemSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MealViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

class MealPlanViewSet(viewsets.ModelViewSet):
    serializer_class = MealPlanSerializer
    # include the premium write permisson
    permission_classes = [IsAuthenticated, IsPremiumOrReadOnly]

    # Override get_queryset to filter meal plans by the authenticated user
    def get_queryset(self):
        # This ensures that users only see their own meal plans
        return MealPlan.objects.filter(user=self.request.user)
    
    # Automatically associate the meal plan with the authenticated user on creation
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MealPlanItemViewSet(viewsets.ModelViewSet):
    serializer_class = MealPlanItemSerializer
    permission_classes = [IsAuthenticated, IsPremiumOrReadOnly]

    # filter meal plan items by the authenticated user's meal plans
    def get_queryset(self):
        return MealPlanItem.objects.filter(meal_plan__user=self.request.user)
