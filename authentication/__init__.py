#!/usr/local/bin/python3
# coding: UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2017-06-10 15:36
# Last modified: 2017-06-11 08:49
# Filename: __init__.py
# Description:
USER_LEVEL_E = 0
USER_LEVEL_A = 9
USER_LEVEL_S = 10
USER_LEVELS = (
    (USER_LEVEL_E, '普通用户'),
    (USER_LEVEL_A, '平台管理员'),
    (USER_LEVEL_S, '系统管理员'),
)

ORDINARY_REDIRECT = 'bills_sheet_list'
ADMIN_REDIRECT = 'expense_admin:bills_sheet_list'


LOGIN_REDIRECTS = {
    USER_LEVEL_S: ADMIN_REDIRECT,
    USER_LEVEL_A: ADMIN_REDIRECT,
    USER_LEVEL_E: ORDINARY_REDIRECT,
}
