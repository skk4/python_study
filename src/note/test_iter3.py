'''
i = 'xieshangji'
print reversed(i)
for e in reversed(i):
    print e
'''    

class MyRev(object):
    def __init__(self, string):
        self.list = list(string)
   
        
    def __iter__(self):
        return self
    
    def next(self):
        if len(self.list): 
            return self.list.pop()
        
        else:
            raise StopIteration
            

    
    
    
myrev = MyRev('xieshangji')
for e in myrev:
    print e    
        
            