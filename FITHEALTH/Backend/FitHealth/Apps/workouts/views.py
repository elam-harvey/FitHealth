from rest_framework.permissions import IsAuthenticated
from FITHEALTH.Backend.FitHealth.Apps.meals.permissions import IsPremiumOrReadOnly
from .models import Workout, WorkoutPlan, WorkoutPlanItem
from .serializer import WorkoutSerializer, WorkoutPlanSerializer, WorkoutPlanItemSerializer
from rest_framework import viewsets
# Create your views here.

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    permission_classes = [IsAuthenticated, IsPremiumOrReadOnly]
    serializer_class = WorkoutSerializer

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsPremiumOrReadOnly]
    serializer_class = WorkoutPlanSerializer

    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)
    
    # Automatically associate the workout plan with the authenticated user on creation
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorkoutPlanItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsPremiumOrReadOnly]
    serializer_class = WorkoutPlanItemSerializer

    def get_queryset(self):
        return WorkoutPlanItem.objects.filter(workout_plan__user=self.request.user)
