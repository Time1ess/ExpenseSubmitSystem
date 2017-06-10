#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-09 10:19
# Last modified: 2017-06-10 15:27
# Filename: views.py
# Description:
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http import HttpResponse, Http404, JsonResponse

from . import _BILL_TYPES_DESC, ESTATUS_SUBMIT, ESTATUS_AMEND
from .models import BillSheet, BillInfo
from .forms import BillInfoMultiForm


class BillsSheetList(LoginRequiredMixin, ListView):
    model = BillSheet
    login_url = reverse_lazy('login')
    paginate_by = 10

    def get_queryset(self):
        return BillSheet.objects.filter(user__auth=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ESTATUS_SUBMIT'] = ESTATUS_SUBMIT
        context['ESTATUS_AMEND'] = ESTATUS_AMEND
        return context


class BillsSheetCreate(LoginRequiredMixin, CreateView):
    model = BillSheet
    template_name = 'bills/billsheet_edit.html'
    fields = []

    def get_context_data(self, *args, **kwargs):
        context = {}
        formset = kwargs.pop('form', None)
        if not formset:
            context = super().get_context_data(*args, **kwargs)
            context['field_descriptions'] = _BILL_TYPES_DESC
            formset = BillInfoMultiForm(queryset=BillInfo.objects.none())
        context['formset'] = formset
        return context

    def post(self, *args, **kwargs):
        formset = BillInfoMultiForm(self.request.POST)
        if formset.is_valid():
            bill_sheet = BillSheet.objects.create(
                user=self.request.user.user,
                count=0, amount=0,
                status=ESTATUS_SUBMIT)
            bill_infos = formset.save(commit=False)
            for bill_info in bill_infos:
                bill_info.sheet = bill_sheet
                bill_info.save()
            bill_sheet.save()
            return redirect('bills_sheet_detail', permanent=True,
                            uid=bill_sheet.uid)
        else:
            return self.form_invalid(formset)


class BillsSheetDetail(LoginRequiredMixin, DetailView):
    model = BillSheet
    slug_field = 'uid'
    slug_url_kwarg = 'uid'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object'].billinfos = context['object'].billinfo_set.all()
        return context


class BillsSheetUpdate(LoginRequiredMixin, UpdateView):
    model = BillSheet
    fields = []
    template_name = 'bills/billsheet_edit.html'
    success_url = 'bills_sheet_detail'
    slug_field = 'uid'
    slug_url_kwarg = 'uid'

    def get_context_data(self, *args, **kwargs):
        context = {}
        formset = kwargs.pop('form', None)
        if not formset:
            context = super().get_context_data(*args, **kwargs)
            bill_infos = context['object'].billinfo_set.all()
            formset = BillInfoMultiForm(queryset=bill_infos)
        context['formset'] = formset
        return context

    def form_valid(self, sheet_uid):
        return redirect(reverse(self.success_url, kwargs={'uid': sheet_uid}))

    def post(self, *args, **kwargs):
        formset = BillInfoMultiForm(self.request.POST)
        if formset.is_valid():
            self.object = self.get_object()
            for form in formset.forms:
                if not form.has_changed():
                    continue
                inst = form.save(commit=False)
                inst.sheet = self.object
                inst.save()
            self.object.save()
            return self.form_valid(self.object.uid)
        else:
            return self.form_invalid(formset)


class BillsInfoDelete(LoginRequiredMixin, DeleteView):
    model = BillInfo
    http_method_names = ['get']
    slug_field = 'uid'
    slug_url_kwarg = 'uid'

    def get(self, *args, **kwargs):
        context = {}
        try:
            obj = self.get_object()
            sheet = obj.sheet
            obj.delete()
            if sheet.billinfo_set.count() == 0:
                sheet.delete()
                sheet_deleted = True
            else:
                sheet.save()
                sheet_deleted = False
        except Http404:
            context['msg'] = '删除失败,系统中无此项信息'
            context['status'] = -1
        else:
            context['msg'] = '删除成功, 点击确认进行跳转'
            context['status'] = 0
            context['redirect'] = reverse('bills_sheet_detail',
                                          kwargs={'uid': sheet.uid})
            if sheet_deleted:
                context['msg'] = '删除成功'
                context['status'] = 1
                context['redirect'] = reverse('bills_sheet_list')
        return JsonResponse(context)


class BillsSheetDelete(LoginRequiredMixin, DeleteView):
    model = BillSheet
    http_method_names = ['post']
    slug_field = 'uid'
    slug_url_kwarg = 'uid'
    success_url = reverse_lazy('bills_sheet_list')
