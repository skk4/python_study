#-*-coding-*-

from selenium import webdriver


class TCRepeatLogin():
    def setUp(self):

        #webdriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.222.30.145:9000/"

    def test_(self):
        driver = self.driver
        driver.get(self.base_url)

        #enter username and password
        #driver.find_element_by_id("kw").send_keys()
        #driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        #driver.find_element_by_id("password").clear()
        driver.find_element_by_id("su").click()
       

        #find dialog and check
        #dialogTitle = driver.find_element(By.XPATH,'//html/body/div[7]/div/div/div[1]/h3')
        #dialogTitle =  driver.find_element_by_xpath('//html/body/div[7]/div/div/div[1]/h3')
        #self.assertEqual("Sign in",dialogTitle.text)

        #find cancel button and click
        #cancelBtn = driver.find_element_by_xpath('//html/body/div[7]/div/div/div[3]/button[2]')
        #cancelBtn.click()

    def tearDown(self):
        self.driver.close()

#if __name__ == "__main__":
# unittest.main()