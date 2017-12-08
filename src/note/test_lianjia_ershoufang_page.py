# -*- coding:utf-8 -*-
import urllib2
import logging
import random
import time
import os
def save_html_file(url, page_num, city, dist):  
    #user_agent ='"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'  
    #headers = { 'User-Agent' : user_agent }
    #iplists = ['117.28.145.96:21400']
    #iplists = ['111.13.7.120:80']
    iplists =  ['121.42.233.165:80', '116.199.115.78:80', '221.229.18.95:808', '111.13.7.120:80','122.228.253.55:808', '106.39.160.135:8888', '122.228.25.97:8101', '115.236.92.74:8088']
    #iplists = ['115.236.92.74:8088']
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
    
    proxy = {'http': random.choice(iplists)} 
    print "proxy-ip:", proxy
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support) 
    opener.addheaders = [('User-Agent', random.choice(user_agent_list)),
                         ('Referer', 'https://'+city+'.lianjia.com/ershoufang/')]
    urllib2.install_opener(opener)
    maxTryNum=2  
    for tries in range(maxTryNum):  
        try:  
            time.sleep(5)
            req = urllib2.Request(url) 
            time.sleep(5) 
            html=urllib2.urlopen(req).read() 
            break  
        except:  
            if tries <(maxTryNum-1):  
                continue  
            else:  
                logging.error("Has tried %d times to access url %s, all failed!",maxTryNum,url)  
                break  
    if 'IP' in html:
        print 'via fail'
        return 0
    else:                    
        file = 'd://lianjia_'+city+'//'+city+'_'+dist+'_' + str(page_num) +'.html'              
        with open(file , 'w') as f:
            f.write(html)
            
              
        print '%s html file saved.' % page_num  
        return 1 
    
def read_html(file): 
    with open(file, 'r') as f:
        html = f.read()
    return html


if __name__ == '__main__' :      
    #url = "https://xm.lianjia.com/ershoufang/siming/pg1"
    city = 'cd'
    dist = 'shuangliu'
    file = 'd://lianjia_'+city
    if os.path.isdir(file):
        pass
    else:
        os.mkdir(file)

    for i in range(1, 27):
        page_file = 'd://lianjia_'+city+'//'+city+'_'+dist+'_' + str(i) +'.html'
        
        url = 'https://'+city+'.lianjia.com/ershoufang/'+dist+'/pg'+str(i)
        time.sleep(3)
        if not os.path.exists(page_file):
            save_result = save_html_file(url, i, city, dist)
            if save_result == 0:
                print 'over'
                break
            else:
                print 'page %s saved.' % i
                time.sleep(5)
        else:
            print 'had download....'    
    print 'ok'        
    
    
            


