# -*- coding:utf-8 -*-
'''
Created on 2017年7月7日

@author: Administrator
'''
from framework.get_testsuite import TestSuites
from framework.excelparser import ExcelParser
from framework.get_teststeps import TestSteps
from framework.get_keycases import KeyCases
from pageobjects.baidu_homepage import HomePage
class DoAction(object):
    def play(self):
        hp = HomePage(self)
        action_list = KeyCases().key_case_list()
        print action_list
        for i in range(len(action_list)):
            if action_list[i][0] == 'type':
                print 'type %s' % action_list[i][1]
                
            
            elif action_list[i][0] == 'search' :
                print 'search %s' % action_list[i][1]
               
            elif action_list[i][0] == 'assert':
                print 'assert %s' % action_list[i][1]
            
            else:
                print 'invalid method' 
            
DoAction().play()               