# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLParser import HTMLParser
import time
#dcap = dict(DesiredCapabilities.PHANTOMJS)
#dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
#dcap["phantomjs.page.customHeaders.User-Agent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0")
#driver = webdriver.PhantomJS(desired_capabilities = dcap) 
#driver.set_page_load_timeout(5)
desired_capabilites = DesiredCapabilities.PHANTOMJS.copy()
headers = {
     'Referer':'http://fanyi.youdao.com/?keyfrom=dict2.index/',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'  
    }

for key, value in headers.iteritems():
    desired_capabilites['phantomjs.page.customHeaders.{}'.format(key)] = value
desired_capabilites['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
desired_capabilites['phantomjs.page.customHeaders.Referer'] = 'http://fanyi.youdao.com/?keyfrom=dict2.index/'   
driver = webdriver.PhantomJS(desired_capabilities=desired_capabilites)
driver.get("http://fanyi.youdao.com/?keyfrom=dict2.index")
time.sleep(5)
driver.maximize_window() #奇葩，不加会报错
driver.set_page_load_timeout(10)
cap_dict = driver.desired_capabilities
for key in cap_dict:
    print '%s: %s' % (key, cap_dict[key])
data = driver.title
print data
driver.find_element_by_id('inputText').send_keys('me')
time.sleep(5)
driver.find_element_by_id('translateBtn').click()
time.sleep(5)
html = driver.page_source
print html
driver.save_screenshot('youdao2.png')
driver.quit()
