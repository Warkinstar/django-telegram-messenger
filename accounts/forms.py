from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    tg_user_id = forms.CharField(
        max_length=50,
        required=False,
        label="Ваш пользовательский ID в телеграмме",
        help_text="Ваш уникальный идентификационный номер пользователя телеграмма."
        " Он необходим для отправки вам сообщений через телеграмм бот."
        " Свой ID можно узнать здесь https://t.me/getmyid_bot/",
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.tg_user_id = self.cleaned_data["tg_user_id"]
        user.save()
        return user
