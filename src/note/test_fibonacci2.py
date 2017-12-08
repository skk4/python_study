# -*- coding:utf-8 -*-
'''
解题思路：
f(n) = f(n-1) + f(n-2)
''' 
def f(n):
    
    if n ==1:
        return n
    if n == 2:
        return n-1
    else:
        return f(n-1)+f(n-2)
    
print f(35)    