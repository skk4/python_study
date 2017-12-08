# -*- coding:utf-8 -*-
'''
递归方式：
10! = 10* (10-1)!
f(n) = n*f(n-1)
'''
def f(n):
    
    if n ==1:
        return n
    else:
        return n*f(n-1)
    
print f(5)    