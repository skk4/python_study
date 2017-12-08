# -*- coding:utf-8 -*-
def gcd(a, b):   
    while 1:
        a = a%b   
        if a == 0:
            return b
            break           
        else:
            b = b%a       
            if b == 0:
                return a
                break            
x = 49
y = 14
print '%d 和 %d 最大公约数为：%d' %(x, y, gcd(x, y))
#49 和 14 最大公约数为：7

    



