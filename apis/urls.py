from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users", views.UserAPIViewSet, basename="customuser")
router.register("user-messages", views.UserMessageAPIViewSet, basename="user-message")

app_name = "apis"

urlpatterns = [
    path("", include(router.urls))
]

# urlpatterns += router.urls