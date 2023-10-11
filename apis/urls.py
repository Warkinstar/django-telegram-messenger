from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("users", views.UserAPIViewSet, basename="user")

app_name = "apis"

urlpatterns = [

]

urlpatterns += router.urls