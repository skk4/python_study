# -*- coding:utf-8 -*-

def my_fun1():
    x = [5]
    def my_fun2():
        x[0] *= x[0]
        return x[0]
    return my_fun2()

my_fun1()

'''
def my_fun1():
    x = 5
    def my_fun2():
        nonlocal x
        x *= x
        return x
    return my_fun2()
my_fun1()
'''