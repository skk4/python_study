'''
Created on 2017.7.7

@author: Administrator
'''
#-*- coding:utf-8 -*-
import xlrd
import xlwt
import os.path

class ExcelParser(object):
    
    def __init__(self, excel_path, sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # ��ȡ��һ����Ϊkeyֵ['ID', 'Selector']
        self.keys = self.table.row_values(0)
        # ��ȡ������,[3]
        self.rowNum = self.table.nrows
        # ��ȡ������,[2]
        self.colNum = self.table.ncols
        
    def dict_data(self):
        if self.rowNum <= 1:
            print("������С��1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # �ӵڶ���ȡ��Ӧvaluesֵ,['type', 'kw']
                values = self.table.row_values(j)
                #self.colNum = 2
                for x in range(self.colNum):
                    #values[0] = 'type'; values[1] = 'kw'
                    #self.keys =['ID', 'Selector']
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

        
if __name__ == "__main__":
    filePath = r"D:\je_workspace\PythonCase\src\excel\testcase.xlsx"
    sheetName = "TestSuite"
    data = ExcelParser(filePath, sheetName)