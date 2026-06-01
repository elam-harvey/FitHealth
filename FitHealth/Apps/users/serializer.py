from rest_framework import serializers
from .models import User, UserSettings, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
           **validated_data
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['user', 'goal', 'current_weight', 'target_weight', 'height', 'age', 'gender', 'activity_level', 'medical_conditions']
        read_only_fields = ['user']

class UserSettingsSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    class Meta:
        model = UserSettings
        fields = ['meal_reminders_time', 'notifications_enabled', 'dark_mode_enabled', 'hydration_reminders_enabled', 'user']
        read_only_fields = ['user']
