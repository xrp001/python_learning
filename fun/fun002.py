# coding: utf-8
def enroll(name, gender, age=12, city="Beijing"):
    print "name:", name
    print "gender:", gender
    print "age:", age
    print "city:", city


def calc(number):
    sum = 0
    for i in number:
        sum = sum + i * i
    return sum


def calc2(*number):
    sum = 0
    for i in number:
        sum = sum + i * i
    return sum


def person(name, age, **kwargs):
    print "name:", name, "age:", age, "others:", kwargs
