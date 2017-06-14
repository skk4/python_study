#-*- conding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url= "http://www.gray.yoya.com"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(50)
driver.find_element_by_id("_yoya_login").click()
driver.find_element_by_id("_pop_user_name").send_keys("xiesj")
driver.find_element_by_id("_pop_password").send_keys("123456")
driver.find_element_by_id("_pop_user_login").click()
driver.implicitly_wait(50)
topmenu=driver.find_element_by_id("top_head_img")
hov= ActionChains(driver).move_to_element(topmenu)
hov.perform()
time.sleep(5)
driver.find_element_by_id("top_ssoLogoutId").click()





