# -*- coding:utf-8 -*-
class Rectangle(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getArea(self):
        return self.x * self.y
    
    def __setattr__(self, name, value):
        if name == 'square':
            self.x = value
            self.y = value
            
        else:    
        
            return object.__setattr__(self, name, value)
    
    
    
re = Rectangle(3, 4)
re.square = 5
print re.getArea()
        