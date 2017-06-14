#-*- conding=utf-8 -*-
class A():
    def add(self,a,b):
        return a+b
    
class B():
    def sub(self,a,b):
        return a-b
count= B()
print count.add(3, 5)
print count.sub(4, 5)
