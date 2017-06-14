# -*- coding=utf-8 -*-
from selenium import webdriver
import time
url="http://www.youdao.com"
dr = webdriver.Chrome()
dr.get(url)
dr.implicitly_wait(30)
dr.find_element_by_id("translateContent").send_keys("hello")
time.sleep(5)
dr.find_element_by_xpath("//*[@id='form']/button").click()
