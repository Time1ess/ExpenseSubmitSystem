#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-08 21:16
# Last modified: 2017-06-11 09:49
# Filename: filters.py
# Description:
from django import template

register = template.Library()
@register.filter('addcls')
def addcls(field, cls):
    return field.as_widget(attrs={"class": cls})
