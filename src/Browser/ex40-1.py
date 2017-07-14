# -*- coding=utf-8 -*-
'''
Created on 2017.7.7

@author: Administrator
'''
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import os
from framework.excelparser import ExcelParser
from framework.get_testsuite import TestSuites
rb = open_workbook(r'D:\testcase.xlsx')
wb = copy(rb)
sheet = wb.get_sheet(2)
key_tuple = TestSuites().yes_testcase_result().items()
len(key_tuple)
for i in range(len(key_tuple)):
    testseq = int(key_tuple[i][0])
    key_tuple[i][1]
    sheet.write(testseq+1, 6, 'pass')
os.remove(r'D:\testcase2.xlsx')
wb.save(r'D:\testcase2.xls')     
    
'''    
sheet.write(1, 6, 'pass')
os.remove(r'D:\testcase2.xlsx')
wb.save(r'D:\testcase2.xls')
'''
