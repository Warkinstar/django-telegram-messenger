from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users", views.UserAPIViewSet, basename="customuser")
router.register("user-messages", views.UserMessageAPIViewSet, basename="user-message")

app_name = "apis"

urlpatterns = [
    path("", include(router.urls)),
    path("users/<pk>/update/", views.UserUpdateAPIView.as_view(), name="user-update"),
]

# urlpatterns += router.urls