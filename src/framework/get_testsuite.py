# -*- coding=utf-8 -*-
'''
Created on 2017.7.7

@author: Administrator
'''
from framework.excelparser import ExcelParser
class TestSuites(object):
    #列表模板[u'test_001', u'test_002', u'test_003', u'test_005']
    def yes_testcase(self):
        filePath = r"D:\je_workspace\PythonCase\src\excel\testcase.xls"
        sheetName = "TestSuite"
        data = ExcelParser(filePath, sheetName)
        p = []
  
        for i in range(len(data.dict_data())):
        #print data.dict_data()[i]['是否执行'.decode('utf-8')]
        
            if data.dict_data()[i]['是否执行'.decode('utf-8')] == 'yes':
                p.append(data.dict_data()[i]['测试用例序列号'.decode('utf-8')])
            
            
        return p
    #字典结构{0: u'test_001', 1: u'test_002', 2: u'test_003', 4: u'test_005'},用例对于表格id
    def yes_testcase_result(self):
        filePath = r"D:\testcase.xlsx"
        sheetName = "TestSuite"
        data = ExcelParser(filePath, sheetName)
        d = {}
  
        for i in range(len(data.dict_data())):
        #print data.dict_data()[i]['是否执行'.decode('utf-8')]
           
        
        
            if data.dict_data()[i]['是否执行'.decode('utf-8')] == 'yes':
                
                
                d.update({i:data.dict_data()[i]['测试用例序列号'.decode('utf-8')]})
                
            
        return d
        
    def get_key(self, dict_data, value):
        self.value = value
        self.dict_data = dict_data
        
        key_list = self.dict_data.keys()
        for i in range(len(self.dict_data)):
            if self.dict_data[key_list[i]] == self.value:
                key = key_list[i]
            
            
        return key 
#print TestSuites().yes_testcase()