#!/usr/bin/env python
# coding=utf-8

' 一个登录验证的demo '
__author__ = 'xiaocai'

import getpass

def input():
    account  = raw_input('account: ')
    password = getpass.getpass('password: ')
    if(account == 'xiaocai' and password == '123123'):
        print 'Login Successful.'
        return True
    else:
        print 'Logon Failure.'
        return False
        pass

input()
# #如果是直接调用这个文件的话
# if __name__=='__main__':
#     input()