from rest_framework import serializers


class AICoachRequestSerializer(serializers.Serializer):
    user_input = serializers.CharField(
        max_length=1000,
        required=True,
        help_text = "Ask FITHEALTH AI Coach a question about your plans"
    )
