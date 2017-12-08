# -*- coding:utf-8 -*-
import urllib2
import logging
import random
import time
def save_house_html_file(url, page_num):
    #user_agent ='"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'
    #headers = { 'User-Agent' : user_agent }
    #iplists = ['111.13.7.120:80']
    iplists =  ['121.42.233.165:80', '116.199.115.78:80', '221.229.18.95:808', '111.13.7.120:80',
                '122.228.253.55:808', '106.39.160.135:8888', '122.228.25.97:8101', '115.236.92.74:8088',
                '218.56.132.154:8080','116.199.2.208:80','45.126.122.117:80', '45.126.122.113:80', 
                '111.13.7.119:80', '45.126.122.112:80', '119.23.161.182:3128', '111.13.7.117:80']
    proxy = {'https': random.choice(iplists)}
    print "proxy-ip:", proxy
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]
    urllib2.install_opener(opener)
    maxTryNum=2
    for tries in range(maxTryNum):
        try:
            time.sleep(2)
            req = urllib2.Request(url)
            time.sleep(2)
            html=urllib2.urlopen(req).read()
            time.sleep(2)
            break
        except:
            if tries <(maxTryNum-1):
                continue
            else:
                logging.error("Has tried %d times to access url %s, all failed!",maxTryNum,url)
                pass
    if 'IP' in html:
        print 'via fail'
        return 0
    else:        

        file = 'd://lianjia_'+city+'_house//'+city+'_'+ dist + '_' + str(page_num) +'.html'
        with open(file , 'w') as f:
            f.write(html)
    
        print '%s html file saved.' % page_num
        return 1

def get_house_ids(file):
    with open(file, 'r') as f:
        html = f.read()
    a = html.find("ids: '")+6
    b = html.find("',", a)
    house_ids = html[a:b].split(',')
    return house_ids
    '''
    house_address =[]
    for house_id in house_ids:
        house_url = 'https://xm.lianjia.com/ershoufang/' + house_id + '.html'
        house_address.append(house_url)

    return house_address
    '''


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


if __name__ == '__main__' : 
    city = 'xm'
    dist = 'huli'
    j = 0 
    for i in range(4, 5):
        time.sleep(2)
        file  = 'd://lianjia_'+city+'//'+city+'_'+dist+'_' + str(i) +'.html'
        house_ids =  get_house_ids(file)
        
        for house_id in house_ids:
            j = j + 1
            house_url = 'https://' + city + '.lianjia.com/ershoufang/' + house_id + '.html'
            time.sleep(2)
            save_result = save_house_html_file(house_url, house_id)
            if save_result == 0:
                print 'over'
                break
            else:
                
                time.sleep(1)
        time.sleep(1)
        print 'page %s save successful!' % i
    
    print '%s house_html save end'  % j
