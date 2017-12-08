# -*- coding:utf-8 -*-
import urllib2
import logging
import random
import time
from xlwt.Workbook import Workbook
from _codecs import encode

def get_house_ids(file):
    try:
        with open(file, 'r') as f:
            html = f.read()
            a = html.find("ids: '")+6
            b = html.find("',", a)
            house_ids = html[a:b].split(',')
            
    except IOError:
        pass
    return house_ids

def get_all_house_ids(city, dist, total_page):
    house_address =[]
    for i in range(1, total_page+1):
        time.sleep(2)
        file  = 'd://lianjia_xm//'+city+'_'+dist+'_' + str(i) +'.html'
        house_ids =  get_house_ids(file)

        house_address = house_ids + house_address

    return house_address

def get_house_html(file):
    with open(file, 'r') as f:
        html = f.read()

    return html

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
    city = 'xm'

    dist = 'huli'
    total_page = 3
    house_ids = get_all_house_ids(city, dist, total_page)
    book = Workbook()
    sheet = book.add_sheet(dist)
    i = 0
    for house_id in house_ids:
        file = 'd://lianjia_xm_house//'+city+'_'+dist+'_' + str(house_id) +'.html'
        html = get_house_html(file)
        house_estate = get_house_estate(html).decode('utf-8')
        print '小区:', house_estate
        house_type = get_house_type(html).decode('utf-8')
        print '类型:', house_type
        house_area = get_area(html).decode('utf-8')
        print '面积：', house_area
        house_perprice = get_per_price(html).decode('utf-8')
        print '单价:', house_perprice
        house_totalprice = get_total_price(html).decode('utf-8')
        print '总价:', house_totalprice
        print '-------***--------'
        sheet.write(i, 0 ,house_estate)
        sheet.write(i, 1 ,house_type)
        sheet.write(i, 2 ,house_area)
        sheet.write(i, 3 ,house_perprice)
        sheet.write(i, 4 ,house_totalprice)
        i = i+1

    file_excel = city + '_' +dist + '.xls'
    book.save(file_excel)
    print 'save ok'
