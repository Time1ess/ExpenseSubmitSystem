#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-10 15:41
# Last modified: 2017-06-10 21:14
# Filename: admin_views.py
# Description:
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from authentication import USER_LEVEL_A

from . import ESTATUS_TYPES
from .views import BillsSheetList, BillsSheetDetail, BillsSheetUpdate


class AdminPermissionRequired(LoginRequiredMixin, PermissionRequiredMixin):
    def has_permission(self):
        # Test if user has high authority
        if self.request.user.user.level >= USER_LEVEL_A:
            return True
        else:
            raise PermissionDenied()


class AdminBillsSheetList(AdminPermissionRequired, BillsSheetList):
    def get_queryset(self):
        return super(BillsSheetList, self).get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['is_admin'] = True
        return context


class AdminBillsSheetDetail(AdminPermissionRequired, BillsSheetDetail):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = True
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        status= request.POST.get('status', None)
        if status not in ESTATUS_TYPES:
            raise PermissionDenied()
        self.object.status = status
        self.object.save()
        return self.render_to_response(self.get_context_data(**kwargs))
