#-*- coding:utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.baidu_homepage import HomePage
from framework.logger import Logger
from selenium import webdriver
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import os
from framework.excelparser import ExcelParser
from framework.get_testsuite import TestSuites
from framework.excelparser import ExcelParser
from framework.get_keycases import KeyCases
from framework.get_teststeps import TestSteps
from framework.get_testsuite import TestSuites



logger = Logger(logger = "BaiduSearch").getlog()

class BaiduSearch(unittest.TestCase):
    
    def setUp(self):
        #unittest.TestCase.setUp(self)
        browse = BrowserEngine('driver')
        print browse
        self.driver = browse.open_browser('driver')
        #self.driver = webdriver.Firefox()
        print self.driver
        
        
        
    def tearDown(self):
        #unittest.TestCase.tearDown(self)
        logger.info("baidu closed......")
        self.driver.quit()    
    '''
    def test_baidu_search(self):
        
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
            
        
        
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        print homepage.type_search('selenium')
        homepage.send_submit_btn()     #调用页面对象类中的点击搜索按钮方法
        print homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
            #excel测试结构标为pass
            
            rb = open_workbook(r"D:\je_workspace\PythonCase\src\excel\testcase.xlsx")
            wb = copy(rb)
            sheet = wb.get_sheet(2)
            sheet.write(1, 6, 'pass')
            os.remove(r"D:\je_workspace\PythonCase\src\excel\testcase.xlsx")
            wb.save(r"D:\je_workspace\PythonCase\src\excel\testcase.xls")
            
        except Exception as e:
            print ('Test Fail.', format(e))
            #excel测试结构标为fail
            
            rb = open_workbook(r"D:\je_workspace\PythonCase\src\excel\testcase.xlsx")
            wb = copy(rb)
            sheet = wb.get_sheet(2)
            sheet.write(1, 6, 'fail')
            os.remove(r"D:\je_workspace\PythonCase\src\excel\testcase.xlsx")
            wb.save(r"D:\je_workspace\PythonCase\src\excel\testcase.xls")
            
            
    def test_baidu_search2(self):
        homepage = HomePage(self.driver)  
        homepage.type_search('python')  # 调用页面对象中的方法  
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法  
        time.sleep(2)  
        homepage.get_windows_img()  # 调用基类截图方法    
        try:
            assert 'python' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
            
            
        except Exception as e:
            print ('Test Fail.', format(e))
            
            
    '''        
             
    def test_case_run(self):
        basepage = BasePage(self.driver)
        ts = TestSuites()
        #excel表内关键字列表 [('type', 'id=>kw', '输入搜索'), (), ()]
        action_list = KeyCases().key_case_list_all()
        test_step_dict = TestSteps().do_teststep_id()
        
        print action_list
        for i in range(len(action_list)):
            if action_list[i][0] == 'type':
                basepage.type(action_list[i][1], 'selenium')
                time.sleep(3)
                print 'selenium %d' %i
                print action_list[i][2]
                x = int(ts.get_key(test_step_dict, action_list[i][2]))
                print 'x:',x
                rb = open_workbook(r"D:\je_workspace\PythonCase\src\excel\testcase.xls")
                wb = copy(rb)
                sheet = wb.get_sheet(3)
                sheet.write(x+1, 5, 'pass')
                os.remove(r"D:\je_workspace\PythonCase\src\excel\testcase.xls")
                wb.save(r"D:\je_workspace\PythonCase\src\excel\testcase.xls")
                time.sleep(3)
                
                
                
                
                
            elif action_list[i][0] == 'search': 
                basepage.click(action_list[i][1])
                time.sleep(3) 
                print 'search'
                x = int(ts.get_key(test_step_dict, action_list[i][2]))
                print 'x:',x
                rb = open_workbook(r"D:\je_workspace\PythonCase\src\excel\testcase.xls")
                wb = copy(rb)
                sheet = wb.get_sheet(3)
                sheet.write(x+1, 5, 'pass')
                os.remove(r"D:\je_workspace\PythonCase\src\excel\testcase.xls")
                wb.save(r"D:\je_workspace\PythonCase\src\excel\testcase.xls")
                time.sleep(3)
                
            else:
                raise NameError ('invalid method')      
            
            
         
         
            
    
    
         
if __name__ == '__main__':
    unittest.main()
    
    
'''
这行代码要注意，意思是到一个页面，第一件事情是初始化这个页面的一个页面对象实例。注意，一定要带self.driver，
不然会报错，这个self.driver，可以这样理解：在当前测试类里面，self.driver是来自浏览器引擎类中方法得到的，
在初始化一个页面对象的时候,也把这个来自浏览器引擎类的driver给赋值给当前的页面对象，这样，才能执行页面对象或者基类里面的相关driver方法。
写多了selenium的自动化脚本，你会明白，最重要的是保持前后driver的唯一性。
'''    