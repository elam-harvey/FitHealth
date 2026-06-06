from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import  status
import jwt
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from FITHEALTH.Backend.FitHealth.Apps.users.models import User
from .models import Register, Login
from rest_framework.views import APIView
from FITHEALTH.Backend.FitHealth.Apps.users.serializer import UserSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    """Handles POST /register/"""
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            # Generate JWT token for the newly registered user
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    """Handles POST /logout/"""
    @extend_schema(request=None, responses={204: None, 200: None})
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
