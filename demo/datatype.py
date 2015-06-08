#!/usr/bin/env python
# coding=utf-8

' 各种数据类型练习 '
__author__ = 'xiaocai'

import getpass

num=1
def tips(msg):
    global num
    print ''
    print '#'+str(num)+'.'+msg+'#'
    num+=1

tips('布尔值是首字母大写')
print True,False

tips('数值1 和 字符"1"不等')
print " 1 == '1' =>", 1=='1'

tips('ASCII编码转换')
print " ord('A') =>", ord('A')
print " chr(65) =>", chr(65)

tips('list有序集合')
names=['X1','X2','S1','S1','S2']
print names
print 'len(names) => ', len(names)
print 'names[0] =>', names[0]
print 'names[-1] =>', names[-1]

names.append("S3")
print 'names.append("S3") =>', names

names.insert(2, "X3")
print 'names.insert(2, "X3") =>', names

names.pop()
print 'names.pop() =>', names

names.pop(3)
print 'names.pop(3) =>', names

names[4]='S3'
print "names[4]='S3'", names

names.sort()
print "names.sort()", names

print "names[0:2]", names[0:2]
print "names[:-1]", names[:-1]
print "names[-1:]", names[-1:]
print "names[::2]", names[::2]

tips('tuple序列表,一旦初始化后不能变更');
names=('X1','X2','X1')
print "names=('X1','X2','X1')",names

tips('循环 for x in ...')
for name in ['X1','X2','S1']:
    print name

tips('循环 while')
names=['X1','X2','S1']
while len(names) > 0:
    print names.pop()

tips('遍历 dict')
sites={'bmp':1,'yyt':2,'apps':{'name':'xx1','ip':'192.168.1.1','host':'ooooo'}}
print sites
for key, value in sites.iteritems():
    print key,' => ',value

tips('dict 使用键-值（key-value）存储')
scores = {'xiaocai':59,'xiaobai':65,'yijian':90}
print scores
print "scores['xiaocai'] => ", scores['xiaocai']
print "'xiaocai' in scores =>", 'xiaocai' in scores
print "scores.get('xiaocai') =>", scores.get('xiaocai')
scores.pop('xiaocai')
print "scores.pop('xiaocai') =>", scores

tips('set集合')
names=set(['X1','X2','X1'])
print "names=set(['X1','X2','X1']) => ",names
names.add('S1')
print "names.add('S1') =>", names
names.remove('S1')
print "names.remove('S1') =>", names



