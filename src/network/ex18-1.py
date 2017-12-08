'''
Created on 2017.7.17

@author: Administrator
'''
import sys, traceback
a = 10
b = 0
try:
    print a/b
except ZeroDivisionError:
    traceback.print_exc()

 