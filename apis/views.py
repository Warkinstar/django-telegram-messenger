from rest_framework import generics, viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
