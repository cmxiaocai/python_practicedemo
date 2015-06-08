#!/usr/bin/env python
# coding=utf-8

import sys

input_argv = sys.argv
if( len(input_argv)==1 ):
    print '''++++++++++++++++++++++++++++++++++++++++++++
学习python过程积累的demo练习
login       模拟用户登录
datatype    数据类型
function    函数调用
object      面向对象
systime     时间处理
exceptions  异常处理
readfile    文件操作
++++++++++++++++++++++++++++++++++++++++++++'''
    sys.exit(0)

module=input_argv[1]

try:
    exec "import demo."+module
except ImportError: 
    print 'Modules do not exist'
    sys.exit(0)

# http://www.w3cschool.cc/python
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000