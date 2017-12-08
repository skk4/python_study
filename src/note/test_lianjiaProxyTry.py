# -*- coding:utf-8 -*-
import urllib2
import logging
import random
import time
def getUrl_multiTry_lianjia(url):  
    #user_agent ='"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'  
    #headers = { 'User-Agent' : user_agent }
    '''
    #iplists =  ['121.42.233.165:80', '116.199.115.78:80', '221.229.18.95:808', '111.13.7.120:80',
                '122.228.253.55:808', '106.39.160.135:8888', '122.228.25.97:8101', '115.236.92.74:8088',
                '218.56.132.154:8080','116.199.2.208:80','45.126.122.117:80', '45.126.122.113:80', 
                '111.13.7.119:80', '45.126.122.112:80', '119.23.161.182:3128', '111.13.7.117:80']
    '''
    user_agent_list =['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"] 
    iplists = ['121.42.233.165:80']
    #iplists = ['218.56.132.154:8080']
    proxy = {'https': random.choice(iplists)} 
    print "proxy-ip:", proxy
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support) 
    opener.addheaders = [('User-Agent', random.choice(user_agent_list)),
                         ('Referer', 'https://xm.lianjia.com/ershoufang/')]
    urllib2.install_opener(opener)
    maxTryNum=2  
    for tries in range(maxTryNum):  
        try:  
            time.sleep(1)
            req = urllib2.Request(url) 
            time.sleep(1) 
            html=urllib2.urlopen(req).read().decode('utf-8')  
            time.sleep(1)
            break  
        except:  
            if tries <(maxTryNum-1):  
                continue  
            else:  
                logging.error("Has tried %d times to access url %s, all failed!",maxTryNum,url)  
                break  
    if 'IP' in html:
        print 'vial fail'
        return 0
    else: 
        return 1                    
    
def getUrl_multiTry_ip(url):  
    #user_agent ='"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'  
    #headers = { 'User-Agent' : user_agent }
    '''
    iplists =  ['121.42.233.165:80', '116.199.115.78:80', '221.229.18.95:808', '111.13.7.120:80',
                '122.228.253.55:808', '106.39.160.135:8888', '122.228.25.97:8101', '115.236.92.74:8088',
                '218.56.132.154:8080','116.199.2.208:80','45.126.122.117:80', '45.126.122.113:80', 
                '111.13.7.119:80', '45.126.122.112:80', '119.23.161.182:3128', '111.13.7.117:80']
    '''
    iplists = ['121.42.233.165:80']
    #iplists = ['218.56.132.154:8080'] 111.13.7.123
    proxy = {'http': random.choice(iplists)} 
    print "proxy-ip:", proxy
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support) 
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]
    urllib2.install_opener(opener)
    maxTryNum=2  
    for tries in range(maxTryNum):  
        try:  
            time.sleep(1)
            req = urllib2.Request(url) 
            time.sleep(1) 
            html=urllib2.urlopen(req).read().decode('utf-8')  
            time.sleep(1)
            break  
        except:  
            if tries <(maxTryNum-1):  
                continue  
            else:  
                logging.error("Has tried %d times to access url %s, all failed!",maxTryNum,url)  
                break  
                   
    return html

def save_html(file):
    with open(file) as f:
        f.write()
        
def open_html(file):
    with open(file) as f:
        f.read()        
if __name__ == '__main__':
    
    
    url = 'http://www.whatismyip.com.tw'
    html = getUrl_multiTry_ip(url)
    a = html.find('"ip-real": "')+12
    print a
    b  = html.find('",', a)
    print b
    print 'real-ip:',html[a:b]
    
    '''
    url2 = "https://xm.lianjia.com/ershoufang/siming/"
    for i in range(1, 2):
        save_result = getUrl_multiTry_lianjia(url2)
        if save_result == 0:
            print 'fail'
        else:
            print i
            
    '''
    '''
    url = 'http://httpbin.org/headers' 
    print getUrl_multiTry_ip(url)
    '''       
