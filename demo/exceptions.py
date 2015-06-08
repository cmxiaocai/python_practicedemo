#!/usr/bin/python
# coding=utf-8

import logging

logging.info('START')

try:
    10 / int('d')
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'No Error'
finally:
    print 'finally...'


class FooError(StandardError):
    pass

try:
    raise FooError('#@@@@')
except FooError, e:
    print '******'
else:
    pass
finally:
    pass


logging.info('END')