#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-08 19:51
# Last modified: 2017-06-10 15:27
# Filename: urls.py
# Description:
from django.conf.urls import url, include

from . import views


bill_sheet_patterns = [
    url(r'^create/$', views.BillsSheetCreate.as_view(), name='bills_sheet_create'),
    url(r'^list/', include([
        url(r'^$', views.BillsSheetList.as_view(), name='bills_sheet_list'),
        url(r'^(?P<page>\d+)/$', views.BillsSheetList.as_view(), name='bills_sheet_list')])),
    url(r'^detail/(?P<uid>.+)/$', views.BillsSheetDetail.as_view(), name='bills_sheet_detail'),
    url(r'^update/(?P<uid>.+)/$', views.BillsSheetUpdate.as_view(), name='bills_sheet_update'),
    url(r'^delete/', include([
        url(r'^$', views.BillsSheetDelete.as_view(), name='bills_sheet_delete'),
        url(r'^(?P<uid>.+)$', views.BillsSheetDelete.as_view(), name='bills_sheet_delete')])),
]

urlpatterns = [
    url(r'^$', views.BillsSheetList.as_view()),
    url(r'^bill_sheet/', include(bill_sheet_patterns)),
    url(r'^bill_info/delete/(?P<uid>.+)/$', views.BillsInfoDelete.as_view(), name='bills_info_delete'),
]
