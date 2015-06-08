#!/usr/bin/env python
# coding=utf-8

' 函数调用相关 '
__author__ = 'xiaocai'


num=1
def tips(msg):
    global num
    print ''
    print '#'+str(num)+'.'+msg+'#'
    num+=1

tips('generator')
g = (x * x for x in range(10))
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()

def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
o.next();
o.next();
o.next();

tips('generator')
def add(x, y, f):
    return f(x) + f(y)
print "add(-999, 100, abs) =>", add(-999, 100, abs)

tips('map')
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

tips('reduce')
def add(x, y):
    return x+y
print reduce(add, [1, 3, 5, 7, 9])

tips('filter')
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

tips('返回函数')
def lazy_sum( *args ):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

fun=lazy_sum(1,2,3,4)
print fun()

tips('匿名函数lambda')
def build(x, y):
    return lambda: x * x + y * y
print build(23,98)
print build(23,98)()

tips('装饰器')
print tips.__name__

tips('偏函数')
import functools
int2 = functools.partial(int, base=2)
print int2('1111')
int16 = functools.partial(int, base=16)
print int16('A')