# -*- coding:utf-8 -*-
class F(object):
    
    def __init__(self):
        self.x = 'FishC'
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
    
    
    def __getattr__(self, name):
        print '该属性不存在'
        #return object.__getattr__(self, name)
        
    def __setattr__(self, name, value):
        return object.__setattr__(self, name, value)    
    
    
    
f = F()
f.x = 'x_man' 
print f.x  
    