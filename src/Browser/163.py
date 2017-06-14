#-*- conding=utf-8 -*-
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains


url= "http://email.163.com"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(30)
driver.find_element_by_id("userNameIpt").send_keys("skk_4")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("skk_198308xie")
driver.find_element_by_id("btnSubmit").click()
driver.implicitly_wait(30)
login_account=driver.find_element_by_id("spnUid").text
driver.quit()

'''
inputname = driver.find_element_by_xpath("//*[@id='idPlaceholder']")
hov=ActionChains(driver).move_to_element(inputname)
hov.perform()
inputname.clear()
inputname.click()
inputname.send_keys("skk_4")
'''
