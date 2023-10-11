from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    tg_user_id = models.CharField(
        "Ваш пользовательский ID в телеграмме",
        max_length=50,
        blank=True,
        help_text="Ваш уникальный идентификационный номер пользователя телеграмма."
        "Он необходим для отправки вам сообщений через телеграмм бот."
        "Свой ID можно узнать здесь https://t.me/getmyid_bot",
    )
