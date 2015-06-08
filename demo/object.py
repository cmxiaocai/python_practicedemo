#!/usr/bin/env python
# coding=utf-8

#http://www.w3cschool.cc/python/python-object.html
__author__ = 'xiaocai'

class Account(object):
    'Optional class documentation string'
    pass

obj = Account
print obj

obj.name = 'xiaocai'
print obj.name

print obj.__doc__

class Account_Entity(object):
    
    def __init__(self, data={}):
        self.__data = data

    #私有的
    def __hasSubAccount(self):
        pass

    def getInfo(self):
        return self.__data

account_entity = Account_Entity({'id':1001, 'name':'xiaocai', 'status':4})
print account_entity.getInfo()

class Account_Action(Account_Entity):
    
    def getInfo(self):
        pass

account_entity = Account_Action({'id':1001, 'name':'xiaocai', 'status':4})
print account_entity.getInfo()

print type(account_entity)
print dir(Account_Action)

print '++++++++++++++++++++++++++++++'

class Parent:        # 定义父类
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr

    def myName(self):
        print '"父类'

class Child(Parent): # 定义子类
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法 child method'

    def myName(self):
        print '子类覆盖父类方法'

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法
c.myName()
