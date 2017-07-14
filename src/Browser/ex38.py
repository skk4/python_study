'''
Created on 2017.7.5

@author: Administrator
'''
class foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def go(self, name, age):
        self.name = 'good'
        self.age = '2' 
        print 'go' + self.name +self.age  
     
        
class done(object):
    def todone(self):
        togo = foo('2', '4').go('2', '4')
        
        
done().todone()
        