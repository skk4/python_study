'''
Created on 2017.6.27

@author: Administrator
'''
'''
def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func(x)
print 'x is still', x
'''
'''
def func():
    global x
    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func()
print 'value of x is:', x
'''

x=6
def f():
    
    global x
    print(x)
    x=2
    
    
f()
print(x)

