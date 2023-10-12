from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    tg_user_id = serializers.CharField(max_length=50)

    def get_cleaned_data(self):
        return {
            "tg_user_id": self.validated_data.get("tg_user_id", ""),
            "username": self.validated_data.get("username", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }

    def custom_signup(self, request, user):
        user.tg_user_id = self.validated_data.get("tg_user_id")
        user.save()
