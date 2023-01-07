# coding: utf-8

# 函数递归
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 高级特性
# 列表生成式
def xx(n):
    L = []
    for i in range(1, n):
        L.append(i * i)
    return L


# 生成器 generator
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
