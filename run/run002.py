# coding: utf-8
from fun.fun002 import enroll, calc, calc2, person

#####################################
enroll("Chris", "M", 14, "Nanjing")
enroll("Dick", "F", city="Nanjing")

#####################################
number_list = [1, 2, 3]
print calc([1, 2, 3])
print calc(number_list)
try:
    print calc()
except:
    print "error"
try:
    print calc(1, 2, 3)
except:
    print "error2"

#####################################
number_list = [1, 2, 3]
try:
    print calc2(1, 2, 3)
except:
    print "error3"
print calc2(*number_list)
print calc2()

#####################################
person("Chris", 12, gender="M", country="China")
person("May", 14, country="USA")
