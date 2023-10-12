from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    fields = ["username", "email", "tg_user_id"]
    template_name = "account/user_update.html"
    success_url = "/"

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj
