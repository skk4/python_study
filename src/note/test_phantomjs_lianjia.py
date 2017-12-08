# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

'''
a= '105101013325,105100851305,105101014076,105100682999'
for i in a.split(','):
    print i
    
    
'''
def open_url(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)  #设置userAgent
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
    #url = "https://xm.lianjia.com/ershoufang/siming/"
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver.set_page_load_timeout(15)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(1)
    pgs = driver.page_source
    return pgs

url = 'https://xm.lianjia.com/ershoufang/siming/pg1'

print open_url(url)