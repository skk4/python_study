# -*- coding:utf-8 -*-
class C(object):  
    def __init__(self):  
        self._x = None 
    #@property     
    def getx(self):  
        print ("get x")  
        return self._x  
    def setx(self, value):  
        print ("set x")  
        self._x = value  
    def delx(self):  
        print ("del x")  
        del self._x  
    x = property(getx, setx, delx, "I'm the 'x' property.")
    
c = C()
c.x # 实例对象访问x属性时，调用getx方法
c.x = 10 # 实例对象赋值x属性时，调用setx方法
#print c._x
#print c.getx()
del c.x  # 实例对象删除x属性时，调用setx方法

'''
当需要更改上例中的getSize、setSize或delSize函数的名称时，如果这些方法是作为接口让用户调用的，
那么对用户而言就要修改自己调用的方法名，很麻烦，使用了proprty()后，用户就不需担心这种问题了。
'''