#-*-coding=utf-8-*-
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver= webdriver.Chrome()
file_path = 'file:///'+ os.path.abspath('checkbox.html')
print file_path
driver.get(file_path)
driver.implicitly_wait(10)
inputs= driver.find_elements_by_tag_name("input")
for i in inputs:
    print i.get_attribute('type')=='checkbox'
    i.click()


