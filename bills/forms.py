#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-09 17:45
# Last modified: 2017-06-10 11:07
# Filename: forms.py
# Description:
from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory, BaseModelFormSet
from django.core.exceptions import ValidationError

from .models import BillInfo


class BillInfoForm(ModelForm):
    class Meta:
        model = BillInfo
        fields = ['type', 'count', 'amount', 'desc']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


BillInfoMultiForm = modelformset_factory(
    BillInfo, form=BillInfoForm, extra=0, min_num=1)
