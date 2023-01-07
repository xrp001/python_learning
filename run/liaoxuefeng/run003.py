# coding: utf-8
import os

from func.liaoxuefeng.fun003 import fact, xx, odd

#####################################
print(fact(5))

#####################################
# 高级特性
# 切片
L = ["Michael", "Sarah", "Tracy", "Bob", "Jack"]
N = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L == N)
print(L[0:2])  # 从索引0开始，直到索引2为止，但不包括索引2。即索引0、1。
print(L[:2] ) # 从索引0开始，直到索引2为止，但不包括索引2。即索引0、1。
print(L[-2:-1])
print(L[-2:-1])

#####################################
# 迭代
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# 迭代key值
for key in d:
    print(key)
# 迭代value值
for value in d.items():
    print(value)

print(d.values())
print(d.keys())

for x, y in [(1, 1), (2, 2), (3, 3), (4, 4)]:
    print(x, y)

#####################################
# 列表生成式
print(range(1, 11))

L = []
for i in range(1, 11):
    L.append(i * i)
print(L)

print(xx(20))

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])

print([d for d in os.listdir('..')])

M = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in M if isinstance(s, str)])

#####################################
# 生成器
g = (x * x for x in range(10))
print(g)
for i in g:
    print(i)

o = odd()
next(o)
next(o)
next(o)

#####################################
