# -*- coding:utf-8 -*-
class F(object):
    count = 0
    def __init__(self):
        
        F.count += 1
        
        
    def __del__(self):
        F.count += 1
        
        
        
        


a = F()
b = F()
c = F()

print F.count

del a
del b
del c
print F.count


s ='a'
a = isinstance(s, str)
print a

print ord(s)


