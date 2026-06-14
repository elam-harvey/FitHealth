from rest_framework.views import APIView
from rest_framework.response import Response
from .ai_services import GeminiCoachService
from rest_framework import status, viewsets
from rest_framework import permissions
from drf_spectacular.utils import extend_schema
from .serializers import AICoachRequestSerializer


class AICoachViewset(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AICoachRequestSerializer

    @extend_schema(
        request=AICoachRequestSerializer,
        summary="Send a message to the AI Fitness Coach",
        description="Expects a JSON body with a 'user_input' key."
    )

    def create(self, request):
        """Handle POST requests to generate coaching responses."""
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_input = serializer.validated_data['user_input']
        coach_service = GeminiCoachService()
        response = coach_service.generate_coaching_response(request.user, user_input)
        return Response({"response": response}, status=status.HTTP_200_OK)
    
