# coding: utf-8
from string import lower, upper

from fun.fun004 import add, f, add2, fn, char2num

#####################################
# 传入函数
print add(5, -6, abs)

#####################################
# map/reduce
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print reduce(add2, [1, 3, 5, 7, 9])

print reduce(fn, [1, 3, 5, 7, 9])
print map(char2num, '13579')
print reduce(fn, map(char2num, '13579'))
# ss = lower('adefD')
# s = list(ss)
# print ss
# print s
# s[0] = upper(s[0])
# str1 = ""+s
#
# print s
# print str1
#####################################

#####################################

#####################################

#####################################

#####################################

#####################################

#####################################
