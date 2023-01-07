# coding:utf-8

# 默认参数
def power(xx, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * xx
    return s
