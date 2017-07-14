# -*- coding:utf-8 -*-
'''
Created on 2017.7.7

@author: Administrator
'''
from framework.get_testsuite import TestSuites
from framework.excelparser import ExcelParser
class TestSteps(object):
    #['输入搜索', '点击搜索', '输入用户名及密码'......]
    def do_teststeps(self):
        filePath = r"D:\je_workspace\PythonCase\src\excel\testcase.xls"
        sheetName = "TestSteps"
        data = ExcelParser(filePath, sheetName)
        testcase_list = TestSuites().yes_testcase()
        #print testcase_list
        teststeps_list = data.dict_data()
        dosteps_list  = []
        for i in range(len(teststeps_list)):
            if teststeps_list[i]['测试用例号'.decode('utf-8')] in testcase_list:
                dosteps_list.append(teststeps_list[i]['测试步骤描述'.decode('utf-8')])

        return dosteps_list
    #{0:'输入搜索',1:'点击搜索',......}
    def do_teststep_id(self):
        filePath = r"D:\je_workspace\PythonCase\src\excel\testcase.xls"
        sheetName = "TestSteps"
        data = ExcelParser(filePath, sheetName)
        testcase_list = TestSuites().yes_testcase()
        #print testcase_list
        teststeps_list = data.dict_data()
        dosteps_list  = {}
        for i in range(len(teststeps_list)):
            if teststeps_list[i]['测试用例号'.decode('utf-8')] in testcase_list:
                dosteps_list.update({i:teststeps_list[i]['测试步骤描述'.decode('utf-8')]})

        return dosteps_list
        
#print TestSteps().do_teststep_id()  