# -*- coding:utf-8 -*-
#http://fz.maitian.cn/esfall/R1
import urllib2
import threading
import time
class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        
    def run(self):
        apply(self.func, self.args)

def download_html(url, html_file_num):
    print 'download html %s file, start at: %s' % (html_file_num, time.ctime())
    time.sleep(1)
    rq = urllib2.Request(url)
    fd = urllib2.urlopen(rq)
    html = fd.read()
    html_file = 'D://miantian_fz//fz_R1_' +str(html_file_num) +'.html'
    with open(html_file, 'w') as f:
        f.write(html)
        
    print 'download html %s file, end at: %s' % (html_file_num, time.ctime())    
        


if __name__ == '__main__' :
    start_page = 1
    end_page = 10
    t1 = time.time()
    threads = []
    for i in range(start_page, end_page+1):
        url = 'http://fz.maitian.cn/esfall/R1/PG' + str(i)
        #d = threading.Thread(target = download_html, args =(url, i))
        d = MyThread(download_html, args = (url, i))
        threads.append(d)
    for i in range(0, end_page-start_page+1):
        threads[i].setDaemon(True)
        
    for i in range(0, end_page-start_page+1):
        threads[i].start()
        
    for i in range(0, end_page-start_page+1):
        threads[i].join()
    t2 = time.time() 
    t = t2-t1
    print t   
    print 'ok'
       