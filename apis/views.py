from rest_framework import generics, viewsets
from .serializers import UserSerializer, UserMessageSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from accounts.models import UserMessage
import requests
from django.conf import settings


tg_bot_token = settings.TELEGRAM_BOT_TOKEN


class UserAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserMessageAPIViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def send_message_to_bot(self, message, tg_user_id):
        """Делает get запрос в чат-бот, по токену, tg_user_id, message"""
        requests.get(
            f"https://api.telegram.org/bot{tg_bot_token}/sendMessage?chat_id={tg_user_id}&text={message}"
        )

    def perform_create(self, serializer):
        """Связывать текущего пользователя с создаваемым сообщением"""
        message = serializer.validated_data["text"]
        tg_user_id = self.request.user.tg_user_id
        self.send_message_to_bot(message, tg_user_id)
        serializer.save(user=self.request.user)
