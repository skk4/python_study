# -*- coding:utf-8 -*-
'''
Created on 2017.7.7

@author: Administrator
'''
from framework.get_testsuite import TestSuites
from framework.excelparser import ExcelParser
from framework.get_teststeps import TestSteps
class KeyCases(object):
    #最终执行关键字驱动列表,模板[(u'type', u'id=>kw'), (u'search', u"xpath=>//*[@id='su']"), (u'input', u'id=>do')]
    def key_case_list(self):
        filePath = r"D:\je_workspace\PythonCase\src\excel\testcase.xlsx"
        sheetName = "PageElements"
        data = ExcelParser(filePath, sheetName)
        keycase_list = data.dict_data()
        #用例测试步骤表：['输入搜索', '点击搜索', '输入用户名及密码'......]
        do_testkey = TestSteps().do_teststeps()
        do_keylist = []
        for i in range(len(keycase_list)):
            if keycase_list[i]['页面元素'.decode('utf-8')] in do_testkey:
                do_keylist.append((keycase_list[i]['关键字'.decode('utf-8')], keycase_list[i]['元素定位表达式'.decode('utf-8')], keycase_list[i]['页面元素'.decode('utf-8')])) 
            

        return do_keylist
    #excel表内关键字列表 [('type', 'id=>kw', '输入搜索'), (), ()]
    def key_case_list_all(self):
        filePath = r"D:\je_workspace\PythonCase\src\excel\testcase.xls"
        sheetName = "PageElements"
        data = ExcelParser(filePath, sheetName)
        keycase_list = data.dict_data()
        #用例测试步骤表：['输入搜索', '点击搜索', '输入用户名及密码'......]
        do_testkey = TestSteps().do_teststeps()
        do_keylist = []
        for i in range(len(keycase_list)):
            if keycase_list[i]['页面元素'.decode('utf-8')] in do_testkey:
                do_keylist.append((keycase_list[i]['关键字'.decode('utf-8')], keycase_list[i]['元素定位表达式'.decode('utf-8')], keycase_list[i]['页面元素'.decode('utf-8')])) 
            

        return do_keylist
        pass     
    
#print KeyCases().key_case_list_all()
#print KeyCases().key_case_list_all()[0][2]
#print len(KeyCases().key_case_list_all())
#print range(3)       