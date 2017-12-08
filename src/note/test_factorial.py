# -*- coding:utf-8 -*-
'''
10! =  1*2*3*4*5*...*9*10
n1 = n-1
n2  =n2*n1
n = n1 

'''
def factorial(n):
    if n == 1 or n == 2:
        return n
    else:    
 
        n2 = n
        while 1:

            n1 = n-1
            n2 =n2*n1
            n = n1
            if n== 2:
                return n2
   
print factorial(5)