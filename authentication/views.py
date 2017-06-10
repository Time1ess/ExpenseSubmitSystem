#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-08 19:57
# Last modified: 2017-06-10 15:40
# Filename: views.py
# Description:
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login

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
        login(self.request, user)
        return super().form_valid(form)
