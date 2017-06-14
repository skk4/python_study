
#-*- conding=utf-8 -*-

from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
#import time
#import os
driver = webdriver.Chrome()
first_url = 'http://www.baidu.com'
print "now access %s" %(first_url)
driver.get(first_url)
driver.implicitly_wait(30)
sencod_url ='http://news.baidu.com'
print "now access %s" %(sencod_url)
driver.get(sencod_url)
driver.implicitly_wait(30)
print "back to %s" %(first_url)
driver.back()
driver.implicitly_wait(30)
print "forword to %s" %(sencod_url)
driver.forward()
driver.implicitly_wait(30)
driver.quit()



