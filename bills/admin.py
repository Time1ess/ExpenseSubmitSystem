#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-09 11:17
# Last modified: 2017-06-09 21:59
# Filename: admin.py
# Description:
from django.contrib import admin

from .models import BillSheet, BillInfo


@admin.register(BillInfo)
class BillInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(BillSheet)
class BillSheetAdmin(admin.ModelAdmin):
    pass
