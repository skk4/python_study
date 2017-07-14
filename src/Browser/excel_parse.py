# -*- coding:utf-8 -*-
'''
Created on 2017.7.6

@author: Administrator
'''
import xlrd
fname = "D:/testcase.xlsx"
bk = xlrd.open_workbook(fname)
sh = bk.sheet_by_name("PageElements")
sh_testsuite = bk.sheet_by_name("TestSuite") 
nrows = sh.nrows
ncols = sh.ncols
print nrows
print ncols
list = []
for i in range(nrows):
    rows =sh.row_values(i)
    print rows

    
'''    
row0 = sh.row_values(0)
row1 = sh.row_values(1)
col0 =sh.col_values(0)
col1 =sh.col_values(1)
print 'clos0:',col0
print 'clos1:',col1
print 'row0:',row0
print row0[1]
'''
