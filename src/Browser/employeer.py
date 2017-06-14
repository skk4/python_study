#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
'''
Created on 2017��5��25��

@author: Administrator
'''

class Employeer():
    '''
    ����Ա������
    '''
    empCount=0


    def __init__(self, name, salary):
        '''
        ��ʼ������
        '''
        self.name = name
        self.salary = salary
        Employeer.empCount+=1
        
    def displayCount(self):
        print "Total Employeer %d" % Employeer.empCount
    def displayEmployeer(self): 
        print "name :", self.name, ", salary:", self.salary
        
"���� Employeer ��ĵ�1������"
emp1=Employeer("andrew",20000)
"���� Employeer ��ĵ�2������"
emp2=Employeer("jim",15000)

emp1.displayEmployeer()
emp2.displayEmployeer()
print  "Total Employee %d" % Employeer.empCount
print "Employeer.__doc__:", Employeer.__doc__
print "Employeer.__name__:", Employeer.__name__
print "Employeer.__module__:", Employeer.__module__
print "Employeer.__bases__:", Employeer.__bases__
print "Employeer.__dict__:", Employeer.__dict__
        