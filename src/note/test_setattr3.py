# -*- coding:utf-8 -*-
'''
c = Counter()
c.x = 1
c.counter
1
c.y = 1
c.z = 1
c.counter 
3
'''
class Counter(object):
    counter = 0
    def __setattr__(self, name, value):
        
        Counter.counter = Counter.counter + 1

        return object.__setattr__(self, name, value)
    
    def __delattr__(self, name):
        Counter.counter = Counter.counter - 1
        return object.__delattr__(self, name)
    
    
c = Counter() 
c.x = 1 
c.y = 1
c.z =1
print c.counter 
del c.x 
print c.counter