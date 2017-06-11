#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-08 19:51
# Last modified: 2017-06-10 21:50
# Filename: urls.py
# Description:
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url('^$', views.ExpenseLogin.as_view()),
    url('^accounts/login', views.ExpenseLogin.as_view(), name='login'),
    url('^accounts/logout', auth_views.LogoutView.as_view(next_page='login'),
        name='logout'),
    url('^accounts/register', views.RegisterView.as_view(), name='register'),
]
