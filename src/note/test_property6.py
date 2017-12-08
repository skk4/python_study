# -*- coding:utf-8 -*-
import pickle
import os
class Mydes(object):
    def __init__(self, t):
        self.t = t
        self.name = 'd:\\'+ self.t+'.pkl'
        
        
        
    def __get__(self, instance, owner):
        getline = '获取属性值：%s' % self.t
        with open(self.name, 'wb') as pickle_file:
            pickle.dump(getline, pickle_file)
        return self.t
    
    
    def __set__(self, instance, value):
        self.t = value
        getline = '设置属性值：%s' % self.t
        with open(self.name, 'wb') as pickle_file:
            pickle.dump(getline, pickle_file)
        
        
    
    def __delete__(self, instance):
        del self.t
        os.remove(self.name) 
           



class Test(object):
    x = Mydes('x')
    y = Mydes('y')   
    
    
test = Test()
test.x = '123'
test.x   
test.y = "xieshangji" 
test.y 
del test.x 
del test.y    