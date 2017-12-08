# -*- coding:utf-8 -*-
#http://fz.maitian.cn/esfall/R1
import urllib2
import threading
import time


def download_html(url, html_file_num):
    print 'download html %s file, start at: %s' % (i, time.ctime())
    time.sleep(1)
    rq = urllib2.Request(url)
    fd = urllib2.urlopen(rq)
    html = fd.read()
    html_file = 'D://miantian_fz//fz_R1_' +str(html_file_num) +'.html'
    with open(html_file, 'w') as f:
        f.write(html)
        
    print 'download html %s file, end at: %s' % (i, time.ctime())    
        


if __name__ == '__main__' :
    page = 11
    t1 = time.time()
    threads = []
    for i in range(1, page+1):
        url = 'http://fz.maitian.cn/esfall/R1/PG' + str(i)
        d = threading.Thread(target = download_html, args =(url, i))
        threads.append(d)
        
    for i in range(0, page):
        threads[i].start()
        
    for i in range(0, page):
        threads[i].join()
    t2 = time.time() 
    t = t2-t1
    print t   
    print 'ok'
        
            
                   
#url = 'http://fz.maitian.cn/esfall/R1/PG' + str(page_num)
#html_file = 'D://miantian_fz//fz_R1_' + str(page_num) +'.html'        