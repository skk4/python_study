#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://email.163.com")
class Account():
    def __init__(self,username ='', password = ''):
        self.username = username
        self.password = password
def do_login_as(user_info):
        driver.find_element_by_id("userNameIpt").clear()
        driver.find_element_by_id("userNameIpt").send_keys(user_info.username)
        driver.find_element_by_id("pwdInput").clear()
        driver.find_element_by_id("pwdInput").send_keys(user_info.password)
        driver.find_element_by_id("btnSubmit").click()

admin = Account(username='skk_4',password='skk_198308xie')
#guset = Account(username='guset',password='321')
Account.do_login_as(admin)
#Account.do_login_as(guset)