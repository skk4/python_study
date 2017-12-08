# -*- coding:utf-8 -*-
class F(object):
    
    def __init__(self, *args):
        self.values = [x for x in args ]
        #print self.values# [1, 2, 3, 4, 5, 6]
        self.count = {}.fromkeys(range(len(self.values)), 0)
        #print self.count#{0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
        
        self.key = None
        
        self.change_count ={}
        
        
    def __len__(self):
        return len(self.values)
    
    
    def __getitem__(self, key):
        self.key = key
        self.count[self.key] = self.count[self.key] + 1
        return self.values[self.key] 
    
    def __setitem__(self, key, value): 
        self.values[key] = value
        
    def __delitem__(self, key):
        self.key = key
        del self.values[self.key]
        del self.count[self.key]
        if self.key == 0:
            for key2 in range(self.key+1, len(self.count)+1):
                self.change_count[key2-1] = self.count[key2]
            #print self.change_count
        elif self.key == len(self.count)-1:
            for key in range(self.key):
                self.change_count[key]= self.count[key]
            #print self.change_count
    
        else:
            for key3 in range(self.key):
                self.change_count[key3] = self.count[key3]
    
            for key4 in range(self.key+1, len(self.count)+1):
                self.change_count[key4-1] = self.count[key4]
        self.count = self.change_count   
      
        
    def append(self, value):
        self.values = self.values + [value]
        self.count[len(self.values)-1] = 0
        
    
    
    def pop(self):
        del self.values[len(self.count)-1] 
        del self.count[len(self.count)-1]
    
    def extend(self, value):
        self.values = self.values + value
        for key5 in range(len(self.count), len(self.count) + len(value) ):
            self.count[key5]= 0
        
        
      
        
            
        
f=F(1, 2, 3, 4, 5, 6)  

f[1]
f[1]
f[1]
f[2]
f[2]
f[4]
#f[6] = 7
print f.count
print f.values
f.pop()
f.extend([7, 8, 9])
f.append(7)
f[6]
f.append(8)
f[6]
del f[3]
f[3]
print f.count
print f.values  

