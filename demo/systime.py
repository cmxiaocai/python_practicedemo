#!/usr/bin/python
import time
import calendar

print time.time()
print time.localtime(time.time())
print time.asctime( time.localtime(time.time()) )
print calendar.month(2015, 5)

print time.strftime("%Y-%m-%d %H:%M:%S")
print int(time.time())

print int(time.mktime(time.strptime('2015-5-26 18:26:30','%Y-%m-%d %H:%M:%S')))
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1432635990))