# -*- coding:utf-8 -*-
def Foo(a):
    try:
        if isinstance(a, str):
            raise TypeError
        
    except TypeError:
        print 'a类型错误'    

Foo('xieshangji')       