#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-08 21:47
# Last modified: 2017-06-10 19:27
# Filename: models.py
# Description:
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User as _User

from . import USER_LEVELS, USER_LEVEL_E


class User(models.Model):
    auth = models.OneToOneField(_User, on_delete=models.CASCADE)
    uid = models.UUIDField(default=uuid4, editable=False, unique=True)
    student_id = models.IntegerField(verbose_name='学号', primary_key=True)
    level = models.IntegerField(verbose_name='权限等级', choices=USER_LEVELS,
                                default=USER_LEVEL_E)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return str(self.student_id)
