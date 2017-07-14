'''
Created on 2017.6.27

@author: Administrator
'''
'''
def add(x):
    x1 = x
    x2 = x*x
    x3 = x*x*x
    return x1, x2, x3
x=5
add(x)
(a, b, c) = add(x)
d = (a, b, c)
print d[0], d[2], d[1]
#print a, b, c
'''
def add(x):
    x1 = x
    x2 = x*x
    x3 = x*x*x
    return x1, x2, x3
x=5
add(x)
[a, b, c] = add(x)
d = (a, b, c)
print d[0], d[2], d[1]
#print a, b, c
