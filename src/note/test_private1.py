# -*- coding:utf-8 -*-
class F(object):
    __name = 10 #双下划线为私有变量
    
    def getname(self):
        return self.__name
    
    
f = F()
print f.getname()  
print f.__name
'''
print f.__name
AttributeError: 'F' object has no attribute '__name'
10
'''