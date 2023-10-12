from django.urls import path, include
from .views import UserUpdateView


urlpatterns = [
    # all path of django-allauth
    path("", include("allauth.urls")),
    path("profile/<pk>/", UserUpdateView.as_view(), name="user_update"),
]