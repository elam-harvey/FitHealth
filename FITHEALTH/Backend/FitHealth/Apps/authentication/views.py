from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import  status
import requests
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from Apps.users.models import User
from rest_framework.views import APIView
from Apps.users.serializer import UserSerializer
from google.oauth2 import id_token
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import Flow

# Create your views here.

User = get_user_model()

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

class LogoutView(generics.CreateAPIView):
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
        
"""class GoogleLoginView(APIView):
    # Handles POST /login/ using an authorization code from the frontend

    def post(self, request):
        # Get the authorization code from the frontend
        authorization_code = request.data["code"]

        if not authorization_code:
            return Response("error: Authorization code not found", status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # initialize the flow using google Client configuration
            flow = Flow.from_client_config(
                client_config={
                    "web": {
                        'client_id' : "",
                        'client_secret' : "",
                        'auth_uri' : 'https://accounts.google.com/o/oauth2/auth',
                        'token_uri' : 'https://oauth2.googleapis.com/token'
                    }
                },
                scopes=["https://www.googleapis.com", "https://www.googleapis.com"],
                redirect_uri = "postmessage"
            )

            # exchange the authorization code for an access token
            flow.fetch_token(authorization_code=authorization_code)
            credentials = flow.credentials

            # securely verify and decode the id token
            id_info = id_token.verify_oauth2_token(
                credentials.id_token,
                Request(),
                "Google_client_id.apps.googleusercontent.com"
            )
            
            email = id_info.get("email")
            name = id_info.get("name")

            # check if the user exists in the database
            user = User.objects.filter(email=email).first()

            if user:
                # if the user exists, return the access token and refresh token
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_201_CREATED)
            else:
                # if the user doesn't exist, create a new user and return the access token and refresh token
                user = User.objects.create_user(email=email, name=name)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": "Invalid authorization code"}, status=status.HTTP_400_BAD_REQUEST)
        """
        
