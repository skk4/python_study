# -*- coding:utf-8 -*-
#http://fz.maitian.cn/esfall/R1
import urllib2
import threading
import time


def download_html(url, html_file_num):
    time.sleep(1)
    rq = urllib2.Request(url)
    fd = urllib2.urlopen(rq)
    html = fd.read()
    html_file = 'D://miantian_fz//fz_R1_' +str(html_file_num) +'.html'
    with open(html_file, 'w') as f:
        f.write(html)
        


if __name__ == '__main__' :
    t1 = time.time()
    threads = []
    for i in range(1, 11):
        url = 'http://fz.maitian.cn/esfall/R1/PG' + str(i)
        download_html(url, i)
        
        
        
    t2 = time.time() 
    t = t2-t1
    print t   
    print 'ok'
        
            
                   
#url = 'http://fz.maitian.cn/esfall/R1/PG' + str(page_num)
#html_file = 'D://miantian_fz//fz_R1_' + str(page_num) +'.html'        