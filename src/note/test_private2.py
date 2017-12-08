# -*- coding:utf-8 -*-
class F(object):
    
    def __x(self):
        print '方法__x'
        
    def x(self):
        print '方法x'
        
    def getx(self):
        self.__x()    
        
f = F()
f.x() 
f.getx()    
#f.__x() 

