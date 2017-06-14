#-*- coding:utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.baidu_homepage import HomePage


logger = Logger(logger = "BaiduSearch").getlog()

class BaiduSearch(unittest.TestCase):
    
    def setUp(self):
        #unittest.TestCase.setUp(self)
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        
         
        
        
    def tearDown(self):
        #unittest.TestCase.tearDown(self)
        logger.info("baidu closed......")
        self.driver.quit()    
    
    def test_baidu_search(self):
        '''
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
            
        '''
        
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()     #调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
            
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
              
if __name__ == '__main__':
    unittest.main()