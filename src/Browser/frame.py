#-*-coding=utf-8-*-
import os
from selenium import webdriver
import time
driver= webdriver.Chrome()
file_path = 'file:///'+ os.path.abspath('frame.html')
print file_path
driver.get(file_path)
driver.implicitly_wait(10)
driver.switch_to_frame("if")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()
