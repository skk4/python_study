# -*- coding:utf-8 -*-
'''
Created on 2017年6月27日

@author: Administrator
'''
from __future__ import division
 
class DivisionException(Exception):
    def __init__(self, x, y):
        Exception.__init__ (self, x, y)       #调用基类的__init__进行初始化
        self.x = x
        self.y = y
 
if __name__ == "__main__":
    
    try:
        x = 3
        y = 2
        if x % y > 0 :
            print "b"                              #如果大于0， 则不能被初始化，抛出异常
            print x/y
            raise DivisionException(x, y)
            print "a"
              
    #except DivisionException, div:                     #div 表示DivisionException的实例对象
    except (DivisionException) as div:                     #div 表示DivisionException的实例对象
        print "DivisionExcetion: x/y = %.2f" % (div.x/div.y)