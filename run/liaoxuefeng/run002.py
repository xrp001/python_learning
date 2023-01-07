# coding: utf-8
from func.liaoxuefeng.fun002 import enroll, calc, calc2, person, fun_multiple_args

#####################################
enroll("Chris", "M", 14, "Nanjing")
enroll("Dick", "F", city="Nanjing")

#####################################
number_list = [1, 2, 3]

print(calc([1, 2, 3]))
print(calc(number_list))
try:
    print(calc())
except:
    print("error")
try:
    print(calc(1, 2, 3))
except:
    print("error2")

#####################################
number_list = [1, 2, 3]
try:
    print(calc2(1, 2, 3))
except:
    print("error3")
print(calc2(*number_list))
print(calc2())

#####################################
person("Chris", 12, gender="M", country="China")
person("May", 14, country="USA")

lee_info = {"city": "Beijing", "job": "student"}
person("Lee", 24, **lee_info)

#####################################
fun_multiple_args(1, 2)
fun_multiple_args(1, 2, 3)
fun_multiple_args(1, 2, 3, "a", "b")
fun_multiple_args(1, 2, 3, "a", "b", x=99)

args = (1, 2, 3, 4)
kw = {"x": 99}
fun_multiple_args(*args, **kw)

#####################################
