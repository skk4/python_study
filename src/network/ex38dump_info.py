# -*- coding:utf-8 -*-
'''
Created on 2017年7月20日

@author: Administrator
'''
import urllib2, sys
hostname =  raw_input(">")
req = urllib2.Request(hostname)
fd = urllib2.urlopen(req)
print "fd:\n", fd
print "Retrieved:" , fd.geturl()
#这个返回对象的字典对象,经典headers对象
info = fd.info()
print "info :\n" , info
print "info items :\n" , info.items()
for key, value in info.items():
    print "-------%s = %s" % (key, value)
