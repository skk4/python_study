'''
Created on 2017.6.30

@author: Administrator
'''
class A(object):
    def __init__(self, name):
        print "enter A"
        print "leave A"
        self.name = name
    def foo(self):
        print self.name
class B(A):
    def __init__(self, name):
        print "enter B"
        A.__init__(self, name)
        print "leave B"    

class C(A):
    def go(self):
        print self.name
        
        
B('bbb').foo()
C("ccc").go()           