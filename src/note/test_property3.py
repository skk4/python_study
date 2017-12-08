class Temprature(object):
    def __init__(self, temp=26.0):
        self.temp = temp
        
    def fget(self):
        return self.temp 
    
    
    def fset(self, value):
        self.temp = value
           
    
    def get(self):
        return self.temp*1.8 + 32
    
    def set(self, value):
        self.temp = (value-32)/1.8
                                
    ces = property(fget, fset, None)
    
    fas = property(get, set, None)
        
t = Temprature()
t.ces = 30.0
print t.fas
print t.ces 
t.fas = 100
print t.ces
print t.fas

 
    
        
    
    
    