# coding: utf-8
from func.liaoxuefeng.fun001 import power

a = 100 + 200
print(a)
print('hello,world')
print('The quick brown fox', 'jumps over', 'the lazy dog')

#####################################
print('100 + 200 =', 100 + 200)

#####################################
# name = raw_input()
# printname

#####################################
print('I\'m ok')

#####################################
a = True
print(type(a))

#####################################
print('''line1
line2
line3''')

#####################################
b = 123
print(b, type(b))
b = 'ABC'
print(b, type(b))

#####################################
x = 10
x = x + 2
print(x)

#####################################
print(power(5, 3))

#####################################
aa = u"厉害了"
bb = u"厉害了"
cc = u"不厉害"
for i in [aa, bb, cc]:
    print(type(i))

print(aa == bb)
print(aa in [bb])
print(aa == cc)
print(aa in [cc])
print(aa == u"厉害了")
print(aa in [u"不厉害"])
