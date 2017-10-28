#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-08 19:57
# Last modified: 2017-06-11 08:49
# Filename: views.py
# Description:
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url

from . import LOGIN_REDIRECTS, USER_LEVEL_E
from .forms import RegisterForm


class RegisterView(CreateView):
    template_name = 'authentication/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('bills_sheet_list')

    def form_valid(self, form):
        username = form.cleaned_data['student_id']
        first_name = form.cleaned_data['student_name']
        password = form.cleaned_data['password']
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name)
        form.instance.auth = user
        login(self.request, user, settings.AUTHENTICATION_BACKENDS[0])
        return super().form_valid(form)


class ExpenseLogin(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        """Ensure the user-originating redirection URL is safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        url_is_safe = is_safe_url(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        user = self.request.user
        if not url_is_safe:
            if user.is_authenticated():
                return reverse(LOGIN_REDIRECTS[int(user.user.level)])
            else:
                return reverse(LOGIN_REDIRECTS[USER_LEVEL_E])
        return redirect_to
