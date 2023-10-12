from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class CustomUser(AbstractUser):
    tg_user_id = models.CharField(
        "Ваш пользовательский ID в телеграмме",
        max_length=50,
        blank=True,
        help_text="Ваш уникальный идентификационный номер пользователя телеграмма."
        "Он необходим для отправки вам сообщений через телеграмм бот."
        "Свой ID можно узнать здесь https://t.me/getmyid_bot",
    )


class UserMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="messages", on_delete=models.CASCADE)
    text = models.TextField("Текст сообщения")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user.username} - {self.created}"
