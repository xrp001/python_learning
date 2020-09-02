# coding: utf-8


# 装饰器
def log(func):
    def wrapper(*args, **kwargs):
        print 'call %s()' % func.__name__
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    print '2020-09-03'