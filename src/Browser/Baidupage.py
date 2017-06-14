#-*-coding=utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class BaiduPage():
    url='http://www.baidu.com/'
    username='13606923594'
    password='skk_198308xie'
     
    def __init__(self,dr):
        self.driver=dr  
               
    def search(self,kw):
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element_by_id('kw').send_keys(kw)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
          

    def login(self):            
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
        time.sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys(self.username)
        self.driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys(self.password)
        self.driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
        time.sleep(2)
         
    def __del__(self):
        pass
        #self.driver.quit()
      
           
driver=webdriver.Chrome()
page=BaiduPage(driver)
#page=BaiduPage(driver)
page.search("51cto")
page.login()
driver.quit()


'''

from pageobject_support import callable_find_by as find_by
from selenium import webdriver
import time

class BaiduSearchPage():
 
    def __init__(self, d):
        self._driver = d

    search_box = find_by(id_="kw")
    search_button = find_by(id_='su')
 
    def search(self, keywords):
        self.search_box().clear()
        self.search_box().send_keys(keywords)
        self.search_button().click()


if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.get("https://www.baidu.com")
    BaiduSearchPage(dr).search("selenium")
    time.sleep(3)
    dr.close()
    
'''    