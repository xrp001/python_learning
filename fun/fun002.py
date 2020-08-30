# coding: utf-8


# 函数的参数
def enroll(name, gender, age=12, city="Beijing"):
    print "name:", name
    print "gender:", gender
    print "age:", age
    print "city:", city


# 不可变参数
def calc(number):
    sum = 0
    for i in number:
        sum = sum + i * i
    return sum


# 可变参数
def calc2(*number):
    sum = 0
    for i in number:
        sum = sum + i * i
    return sum


# 关键字参数
def person(name, age, **kwargs):
    print "name:", name, "age:", age, "others:", kwargs


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，
# 这四种参数可以一起使用，或者只使用其中某些，但是请注意，参数的顺序必须是：
# 必选参数、默认参数、可变参数和关键字参数。
def fun_multiple_args(a, b, c=0, *args, **kwargs):
    print "a =", a, "b =", b, "c =", c, "args =", args, "kwargs =", kwargs
