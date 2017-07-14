# -*- coding:utf-8 -*-
'''
Created on 2017年6月27日

@author: Administrator
'''
'''
try:
    file("hello.txt", "r")                  #如果文件不存在，引发异常
    print "读文件"
except IOError:                              #捕获IO异常
    print "文件不存在"
except:                                     #其它异常
    print "程序异常"
    
'''    
'''
另外一个列子
......
'''    
    
try:
    s='hello'
    #s2='good'
    #s = s1-s2
    try:
        
        print s[0] + s[1]
        print s[0] - s[1]
        
    except Exception, e:
        print e.message
        
except Exception, e:
    print e.message
        