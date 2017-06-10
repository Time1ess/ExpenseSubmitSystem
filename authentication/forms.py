#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-08 22:02
# Last modified: 2017-06-09 12:00
# Filename: forms.py
# Description:
from django import forms
from django.forms import ModelForm
from .models import User


class RegisterForm(ModelForm):
    student_id = forms.CharField(
        label='学号',
        widget=forms.TextInput())
    student_name = forms.CharField(
        label='姓名',
        widget=forms.TextInput())
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(),
        min_length=6,
        max_length=20)
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(),
        min_length=6,
        max_length=20)

    class Meta:
        model = User
        fields = ['student_id', 'student_name', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('请确认两次输入密码一致')
        return cleaned_data
