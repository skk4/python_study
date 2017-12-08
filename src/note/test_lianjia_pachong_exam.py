# -*- coding:utf-8 -*-
from xlwt.Workbook import Workbook 
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def open_url(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)  #设置userAgent
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
    #url = "https://xm.lianjia.com/ershoufang/siming/"
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver.set_page_load_timeout(15)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(1)
    pgs = driver.page_source
    return pgs

def city_dist_url(city, dist):
    url = 'https://'+city+'.lianjia.com/ershoufang/' +dist
    return url
    
def get_total_page(html):
    a = html.find('totalPage&quot;')+16
    b = html.find(',&quot;curPage',a)
    total_pg = html[a:b]
    return int(total_pg)

def get_house_page_address(total_page, dist):
    #total_page = get_total_page()
    url_pages = []
    for url_page_id in range(1, total_page+1-73):
        url_page = 'https://'+city+'.lianjia.com/ershoufang/'+dist +'/' +'pg'+ str(url_page_id)
        url_pages.append(url_page)
    return url_pages 

  
def get_house_ids(html):
    a = html.find("ids: '")+6
    b = html.find("',", a)
    house_ids = html[a:b].split(',')
    url_houses = []
    for each_id in house_ids:
        url_house = 'https://xm.lianjia.com/ershoufang/' +each_id +'.html'
        url_houses.append(url_house)
    return url_houses    
        

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


if __name__ == '__main__':
    data = {'xm':'厦门', 'siming':'思明'}
    city = 'xm'
    dist = 'siming'
    house_dist = city_dist_url(city,dist)
    print '城市：%s, 市区：%s' %(data[city], data[dist])
    print '网址:', house_dist 
    #url = "https://xm.lianjia.com/ershoufang/105101013325.html"
    #获取城区各区页面html代码
    html = open_url(house_dist)
    #获取城区各区房源总页数
    total_page = get_total_page(html)
    #打开各区房源各页面
    house_page_nums = get_house_page_address(total_page, dist)
    book = Workbook()
    sheet_sm = book.add_sheet('siming')
    for house_page in house_page_nums:
        print '%s市,%s区,总房源页面地址：%s' %(data[city], data[dist], house_page)
        #获取区房源各分页的html页面代码
        house_page_html = open_url(house_page)
        #获取当前页面的目标房源的访问地址
        target_house_address= get_house_ids(house_page_html)
        i = 0

        for each_target_house in target_house_address:
            target_house_html = open_url(each_target_house)
            print '房源数：%s' %(i+1)
            house_estate = get_house_estate(target_house_html)
            print '小区:', house_estate
            house_type = get_house_type(target_house_html)
            print '类型:', house_type
            house_area = get_area(target_house_html)
            print '面积：',house_area
            house_perprice = get_per_price(target_house_html)
            print '单价:', house_perprice
            house_totalprice = get_total_price(target_house_html)
            print '总价:', house_totalprice
            sheet_sm.write(i,0,house_estate)
            sheet_sm.write(i,1,house_type)
            sheet_sm.write(i,2,house_area)
            sheet_sm.write(i,3,house_perprice)
            sheet_sm.write(i,4,house_totalprice)
            i = i + 1
    book.save('xm.xls')
    print 'saved.'
        
        
        
        
    #获取每页页面房源id
    #get_house_ids(html)
    #print '小区', get_house_estate(html)
    #print '商品房类型', get_house_type(html)
    #print '面积：',get_area(html)
    #print '单价', get_per_price(html)
    #print '总价', get_total_price(html)
    
    

