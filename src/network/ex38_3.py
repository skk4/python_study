# -*- coding:utf-8 -*-

'''
Created on 2017年7月20日

@author: Administrator
'''
'''class A:
    def find_user(self, a1, a2):
        print 'find,a1,a2'
        
    def find_x(self, x1, x2):
        print "findx" '''
from network.ex39 import A
    
class B(A):
    def find_user(self, a1, a2):
        re = A.find_user(self, a1, a2)
        #print  re
        

