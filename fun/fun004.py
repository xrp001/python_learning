# coding: utf-8


# 传入函数
# 一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)


# map/reduce
# rdduce把一个函数作用在一个序列[x1,x2,x3...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的
# 下一个元素做累积运算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


def f(x):
    return x * x


def add2(x, y):
    return x + y


def fn(x, y):
    return 10 * x + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3,
            '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
