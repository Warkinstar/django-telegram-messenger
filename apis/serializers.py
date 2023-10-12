from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import UserMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["pk", "username", "email", "tg_user_id"]


class UserMessageSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = UserMessage
        fields = ["pk", "user", "text", "created", "updated"]

