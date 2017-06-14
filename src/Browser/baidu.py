# -*- conding=utf-8 -*-
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
driver.set_window_size(480, 800)
driver.find_element_by_css_selector(".s_ipt").send_keys("")
driver.quit()