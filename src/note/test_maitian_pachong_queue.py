import threading
import time
import urllib2
import Queue
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
        


class MyDownloadWorker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        while True:
            item = self.queue.get()
            if item is None:
                break
            url, html_file_num = item
            download_html(url, html_file_num)
            self.queue.task_done()
            

if __name__ == '__main__':
    ts1 = time.time()
    queue = Queue.Queue()
    for x in range(5):
        
        worker = MyDownloadWorker(queue)
        worker.daemon = True
        worker.start()
            
    
    for i in range(1, 11):
        
        url = 'http://fz.maitian.cn/esfall/R1/PG' + str(i)
        queue.put((url, i))
    queue.join()    
    ts2 = time.time() 
    ts = ts2 - ts1   
    print 'end' 
    print ts   

        