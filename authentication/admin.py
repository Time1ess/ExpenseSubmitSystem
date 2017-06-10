#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-09 21:58
# Last modified: 2017-06-09 21:59
# Filename: admin.py
# Description:
from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
