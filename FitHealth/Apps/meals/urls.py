from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealViewSet, MealPlanViewSet, MealPlanItemViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'meals', MealViewSet, basename='meal')
router.register(r'meal-plans', MealPlanViewSet, basename='mealplan')
router.register(r'meal-plan-items', MealPlanItemViewSet, basename='mealplanitem')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]