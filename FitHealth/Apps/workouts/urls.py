from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet, WorkoutPlanViewSet, WorkoutPlanItemViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'workout-plans', WorkoutPlanViewSet, basename='workoutplan')
router.register(r'workout-plan-items', WorkoutPlanItemViewSet, basename='workoutplanitem')

urlpatterns = [
    path('', include(router.urls)),
]