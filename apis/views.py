from rest_framework import generics, viewsets
from .serializers import UserSerializer, UserMessageSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from accounts.models import UserMessage


class UserAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserMessageAPIViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Связывать текущего пользователя с создаваемым сообщением"""
        serializer.save(user=self.request.user)
