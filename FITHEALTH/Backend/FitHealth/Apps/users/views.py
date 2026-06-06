from django.shortcuts import render
from .models import User, UserProfile, UserSettings
from .serializer import UserSerializer, UserProfileSerializer, UserSettingsSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.response import Response


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    """Handles GET /me/ and PUT /update/"""
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.userprofile

class UserSettingsDetailView(generics.RetrieveUpdateAPIView):
    """Handles GET /settings/ and PUT /settings/update/"""
    serializer_class = UserSettingsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.usersettings