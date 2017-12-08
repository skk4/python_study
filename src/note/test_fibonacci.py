# -*- coding:utf-8 -*-
'''
1, 1, 2, 3, 5, 8, 13
解题思路：
第一个数a = 1 
第二个数b =
 c = a+b
 a=b
 b=c     
返回c          
'''
def fibo(n):
    
    if n == 1:
        print n
        
    elif n == 2:
        print n-1    
    else:    
        a = 1 
        b=1
        for i in range(1,n):            
            c =0
            if i>=2:
                c = a+b
                a=b
                b=c
    print c  
    
fibo(35)                  