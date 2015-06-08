#!/usr/bin/env python
# coding=utf-8

' 文件读取demo '
__author__ = 'xiaocai'

#read() 、readline()、readlines()
#read()会将所有内容读入到一个字符串中
#readlines()将所有内容按行读取，返回一个列表
#readline()每次读取一行
#read()及readlines()效率高，但是需要内存能放的下
print '只适用于小文件'
file = open("testdata/access_log_1")
while 1:
    line = file.readline()
    if not line:
        break
    print len(line)
file.close()

print '只适用于小文件 (据说大文件时会有问题)'
file = open("testdata/access_log_1")
while 1:
    lines = file.readlines()
    if not lines:
        break
    for line in lines:
        print len(line)
file.close()

print 'fileinput实际效果较慢，但是也有buffer管理功能'
import fileinput
for line in fileinput.input("testdata/access_log_1"):
    print len(line)

print '网络建议的大文件读取方法,最快速的,内存占用小'
file=open("testdata/access_log_1", "r");
for line in file:
    print len(line)
file.close()

print '写文件'
import time
file = open('testdata/access_log_2', 'w')
file.write(time.strftime("%Y-%m-%d %H:%M:%S"))
file.close()

import os
# 查看当前目录的绝对路径:
print os.path.abspath('.')
print os.listdir('.')