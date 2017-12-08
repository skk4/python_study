# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
def foo():
    count = 5
    print count*5
#print count # count为局部变量，无法被外部环境调用


def foo1():
    print '这个是fool函数'
    def foo2():
        print '这个是foo2函数'
    foo2()

foo1()
