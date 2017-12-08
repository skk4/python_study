# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import DesiredCapabilities
from HTMLParser import HTMLParser
import time
class Translator(HTMLParser):
    def __init__(self):
        self.trans_result = ''
        self.read_result = 0
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            #print 'attrs............',attrs
            for x, y in attrs:
                #print x, y
                if y == 'tgt':           
                    self.read_result = 1
            
            
    def handle_data(self, data):
        if self.read_result:
            self.trans_result = data + self.trans_result
             
        
        
    def handle_endtag(self, tag):
        if tag == 'p':
            self.read_result = 0           
            
            
    def gettrans_rusult(self):
        return self.trans_result        

while 1:
    inputword = raw_input('>')
    if inputword == 'q':
        print 'exit'
        break
    else:
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
        driver.set_page_load_timeout(15)
        driver.get("http://fanyi.youdao.com")
        time.sleep(10)
        driver.maximize_window()
        time.sleep(2)
        print driver.title
        #driver.implicitly_wait(15)
        driver.find_element_by_id('inputText').send_keys(inputword.decode('utf-8'))
        print 'input'
        time.sleep(10)
        driver.set_page_load_timeout(15)
        #driver.implicitly_wait(15)
        driver.find_element_by_id('translateBtn').click()
        time.sleep(10)
        print 'click'
        driver.set_page_load_timeout(15)
        time.sleep(10)
        driver.save_screenshot('youdao2.png')
        print 'translate success!'
        html = driver.page_source
        '''
        fd = open(html)
        tp = Translator()
        for each in fd.readlines():
    
            tp.feed(each + '------------\n')
        print 'tp--',tp.gettrans_rusult()
        '''
        
        tp = Translator()
        tp.feed(html)
        print 'tp--',tp.gettrans_rusult() 

        #print html
        driver.quit()
       
