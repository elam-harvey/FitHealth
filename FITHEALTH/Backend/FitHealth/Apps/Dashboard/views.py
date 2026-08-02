from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# import from oter modules
from Apps.workouts.models import WorkoutPlan
from Apps.meals.models import MealPlan
from Apps.AI.ai_services import GeminiCoachService
from django.utils import timezone

# import from current module
from .models import Motivation, Snack, Exercises, ActiveChallenge
from .serializers import DashboardSerializer


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DashboardSerializer

    def get(self, request):
        """Get the user's dashboard data"""
        user = request.user
        today = timezone.now().date()

        # get the user's workout plan
        workout_plan = WorkoutPlan.objects.filter(user=user).first()
        meal_plan = MealPlan.objects.filter(user=user).first()

        # fetch the global read-only data
        motivation = Motivation.objects.order_by('?').first()
        snacks = Snack.objects.filter(is_active=True, date=today).order_by('?')
        exercises = Exercises.objects.filter(is_active=True, date=today).order_by('?')[:3]
        active_challenges = ActiveChallenge.objects.filter(user=user).order_by('?')

        # put the data into a single dictionary
        dashboard_data = {
            "workout": workout_plan,
            "meal": meal_plan,
            "motivation": motivation,
            "snacks": snacks,
            "exercises": exercises,
            "active_challenges": active_challenges,
            "user": user.profile.__dict__
        }

        serializer = DashboardSerializer(dashboard_data)
        return Response(serializer.data)

