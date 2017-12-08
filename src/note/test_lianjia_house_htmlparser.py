# -*- coding:utf-8 -*-
import urllib2
import json
from HTMLParser import HTMLParser 
import time
import random
from xlwt.Workbook import Workbook

# 解析html信息
class Houseaddress(HTMLParser):
    def __init__(self):
        self.set_flag = 0
        #房源id
        self.house_address_id = []
        #总页数
        self.total_page = ''
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            #print 'including attrs.....', attrs
            for x, y in attrs:
                if x == 'data-housecode':
                    #print 'y-----------', y
                    self.house_address_id.append(y)
                    self.house_address_id
                    self.set_flag = 1
                    
        if  tag == 'div':
            for x, y in attrs:            
                if x == 'page-data': 
                    #print 'y-----', y
                    self.total_page = y
                    self.set_flag = 1
                
        #print("Encountered a start tag:", tag)
        
    def handle_data(self, data):
        
        if self.set_flag:            
            pass        
        
    def handle_endtag(self, tag):
        if tag == 'a':
            
            self.set_flag = 0
            
        if tag == 'div':
            self.set_flag = 0
                                     
        #print("Encountered a start tag:", tag)
        
       
            
    def gettrans_rusult(self):
        
        pass
    
    #获取当前页房源id
    def gethousea_ddress_id(self):
        return  list(set(self.house_address_id)) 
    
    #获取当前房源总页数
    def get_total_page(self):
        return json.loads(self.total_page)['totalPage']


#获取当前页html内容       
def my_ip():
    url = 'http://www.whatismyip.com.tw'
    #url = 'http://www.baidu.com'
    iplists = ['121.232.147.119:9000']
    #'119.55.136.97:80',
    proxy = {'http': random.choice(iplists)}
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    '''
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'),
                         ('Referer', 'https://xm.lianjia.com/ershoufang/')]
                         '''
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]
    urllib2.install_opener(opener)
    rq = urllib2.Request(url)
    fd = urllib2.urlopen(rq)
    html = fd.read().decode('utf-8')
    return html
    
def open_url(url):
    
    #iplists = ['183.47.137.90:8118', '223.13.72.8:8118', '119.55.136.97:80', '121.232.147.119:9000']
    iplists = ['111.13.7.42:81']
    proxy = {'http': random.choice(iplists)}
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'),
                         ('Referer', 'https://xm.lianjia.com/ershoufang/')]
    urllib2.install_opener(opener)
    time.sleep(1)
    rq = urllib2.Request(url)
    
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    rq = urllib2.Request(url, headers=headers)
    '''
    time.sleep(1)
    fd = urllib2.urlopen(rq)
    time.sleep(1)
    html = fd.read().decode('utf-8')
    time.sleep(1)
    fd.close()
    return html
    


#获取当前页面的房源id['1000122', '10032243']
def get_house_url_id(url_page):
    #pass
    house_addesses = Houseaddress()
    time.sleep(3)
    house_addesses.feed(open_url(url_page))
    time.sleep(3)
    house_ids = house_addesses.gethousea_ddress_id()
    url_houses = []
    for house_id in house_ids:
         
        url_house = 'https://xm.lianjia.com/ershoufang/' +house_id +'.html'
        url_houses.append(url_house)
    return url_houses
    
    
#获取房源总页数    
def get_total_page():
    house_addesses = Houseaddress()
    house_addesses.feed(open_url(url_page))
    return int(house_addesses.get_total_page())   
 
#进入指定房源页面获取小区名
def get_house_estate(html):    
    a = html.find("resblockName:'") + 14
    b = html.find("',", a)
    return html[a:b]
    
#进入指定房源页面获取房源类型（住宅、商业、别墅、车位等）
def get_house_type(html):
    a = html.find("houseType:'") + 11
    b = html.find("',", a)
    return html[a:b]

#进入指定房源页面获取房源总价    
def get_total_price(html):
    a = html.find("totalPrice:'") + 12
    b = html.find("',", a)
    return html[a:b]

#进入指定房源页面获取房源每平价格        
def get_per_price(html):
    a = html.find("price:'") + 7
    b = html.find("',", a)
    return html[a:b]

#进入指定房源页面获取房源面积    
def get_area(html):
    a = html.find("area:'") + 6
    b = html.find("',", a)
    return html[a:b]
#当前页面所有的房源地址
def get_url_house():
    house_ids = get_house_url_id()
    url_houses = []
    for house_id in house_ids:
         
        url_house = 'https://xm.lianjia.com/ershoufang/' +house_id +'.html'
        url_houses.append(url_house)
    return url_houses    

def get_url_page():
    total_page = get_total_page()
    url_pages = []
    for url_page_id in range(1, total_page+1-73):
        url_page = 'https://xm.lianjia.com/ershoufang/siming/' + 'pg'+ str(url_page_id)
        url_pages.append(url_page)
    return url_pages    

def run_page():
    page_houseids = get_house_url_id()
    for house_id in page_houseids:
        return house_id
        #open_url(get_url)
        


if __name__ == '__main__':
    url_page = 'https://xm.lianjia.com/ershoufang/siming'
    #print my_ip()
    print open_url(url_page) 
    #print get_total_page()      
    #print get_house_url_id()

    #print get_total_page()

    #print get_house_estate()
    #print get_area()
    #print get_house_type()
    #print get_total_price()
    #print get_per_price()
    #open_url(url_house)
    #print get_url_house()

    pages = get_url_page()
    #run_page()
    
    house_urls = []  
    for each_page in pages:
        house_url = get_house_url_id(each_page) 
        #print '页数：%s, 地址集：%s' %(each_page, house_url)
        print '页数:', each_page
        print '房源页面:', house_url
        house_urls = house_url + house_urls 
    print '房源总页面:', house_urls
    
    
    i = 0
    book = Workbook()
    sheet_sm = book.add_sheet('siming')
    for each_house in house_urls:
        time.sleep(3)
        html = open_url(each_house) 
        time.sleep(3)
        print '房源排序号：%s' %(i+1)
        house_estate = get_house_estate(html)
        print '小区:', house_estate
        house_type = get_house_type(html)
        print '类型:', house_type
        house_area = get_area(html)
        print '面积：', house_area
        house_perprice = get_per_price(html)
        print '单价:', house_perprice
        house_totalprice = get_total_price(html)
        print '总价:', house_totalprice
        print '-------***--------'
        sheet_sm.write(i, 0 ,house_estate)
        sheet_sm.write(i, 1 ,house_type)
        sheet_sm.write(i, 2 ,house_area)
        sheet_sm.write(i, 3 ,house_perprice)
        sheet_sm.write(i, 4 ,house_totalprice)
        i = i+1
        time.sleep(2)
        
    book.save('xm3.xls') 
    print 'save ok'  

        
        
       
        
    
    
    
    
    