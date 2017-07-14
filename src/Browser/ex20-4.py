# -*- coding=utf-8 -*-
'''
Created on 2017.6.27

@author: Administrator
'''

'''
a=10
b=0
a/b
print "done"
'''

a=10
b=2
try:
    c=a/b
    print c
except Exception, e:
    print e.message
else:
    print "ok"    
print "done"   

input_value = input(">")
if type(input_value)== type(2):
    print input_value
else:
    raise ValueError