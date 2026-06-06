from django.shortcuts import render
from rest_framework import viewsets
from FITHEALTH.Backend.FitHealth.Apps.meals.permissions import IsPremiumOrReadOnly
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
    permission_classes = [IsAuthenticated, IsPremiumOrReadOnly]

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MealPlanItemViewSet(viewsets.ModelViewSet):
    serializer_class = MealPlanItemSerializer
    permission_classes = [IsAuthenticated, IsPremiumOrReadOnly]

    def get_queryset(self):
        # It hops from MealPlanItem -> MealPlan -> User
        return MealPlanItem.objects.filter(meal_plan__user=self.request.user)