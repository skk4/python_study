#-*- coding:utf-8 -*-

import ConfigParser
import os.path
from selenium import webdriver
from framework.logger import Logger


logger = Logger(logger = "BrowserEngine").getlog()

class BrowserEngine(object):
    
    dir = os.path.dirname(os.path.abspath('.')) #注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    
    def __init__(self, driver):
        self.driver = driver
     
    #读取浏览器配置文件信息，并返回浏览器driver  
    def open_browser(self, driver):
        
        config = ConfigParser.ConfigParser()
        
        #配置文件地址
        #file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        
        config.read(file_path)
        
        #获取配置文件浏览器类型
        browser = config.get("browserType", "browserName")
        logger.info("You had selected %s browser. " % browser)
        
        url = config.get("testServer", "URL")
        logger.info("You had via to %s url." % url)
        
        #浏览器选择判断
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
            
        elif browser == "Chrome":
            #chrome驱动地址 
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting chrome browser.")
            
        elif browser =="IE":
            #IE驱动地址
            driver = webdriver.Ie(self.ie_driver_path)    
            logger.info("Starting ie browser.")
            
            
        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximinze the current windows.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 sec.")   
        return driver
        
        
        
    def quit_browser(self):
        logger.info("Now, close and quit browser.")
        self.driver.quit()
            
        
        
            
        

