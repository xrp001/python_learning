# coding: utf-8
import functools


# 装饰器（Decorator）
# 在代码的运行期间动态增加功能的方式
# 本质上，decorator就是一个返回函数的高阶函数


def log(func):
    def wrapper(*args, **kwargs):
        print('call %s()' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('2020-09-03 now')


def now2():
    print('2020-09-03 now')


def log2(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log2('execute')
def now3():
    print('2020-09-06 now3')


def now4():
    print('2020-09-06 now4')


# def log3(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print 'call %s():' % func.__name__
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log3('execute')
# def now5():
#     print '2020-09-06 now5'


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log4('execute')
def now7():
    print('2020-09-06 now7')


def now8():
    print('2020-09-06 now8')
