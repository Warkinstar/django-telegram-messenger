from django.contrib import admin
from .models import CustomUser, UserMessage

# Register your models here.

admin.site.register(CustomUser)


class AdminUserMessage(admin.ModelAdmin):
    list_display = ["user", "text", "created"]


admin.site.register(UserMessage, AdminUserMessage)
