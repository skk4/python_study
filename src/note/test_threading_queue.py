# -*- coding:utf-8 -*-
import requests
import json
import os
from time import time
from pathlib import Path
from itertools import chain
from Queue import Queue
from threading import Thread
def get_my_links(url):
   
    req = requests.get(url)
    html = req.text
    a = html.find('gallery:')+8
    b = html.find('siblingList:', a)
    url_list = html[a:b-6]
    json_url = json.loads(url_list)
    url_dict = json_url['sub_images']
    down_lists = []
    for each_url_dict in url_dict:
        down_lists.append(each_url_dict['url'])
    return down_lists 

def setup_my_download_dir(directory):
    download_dir = Path(directory)
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir


def download_my_link(directory, link): 
    image_name = '{}.jpg'.format(os.path.basename(link))
    download_path = directory / image_name
    print download_path
   
    r = requests.get(link)
    with download_path.open('wb') as fd:
        fd.write(r.content)


class DownLoadMyWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
       
    def run(self):
        while True:
            item = self.queue.get()
            if item is None:
                break
            directory, link = item
            download_my_link(directory, link)
            self.queue.task_done()  



if __name__ == '__main__':
    ts1 = time()
    url1 = 'http://www.toutiao.com/a6473272326501696014'
    url2 = 'http://www.toutiao.com/a6333981316853907714'
    url3 = 'http://www.toutiao.com/a6313664289211924737'
    url4 = 'http://www.toutiao.com/a6334337170774458625'
    url5 = 'http://www.toutiao.com/a6444769472229277965'
    download_dir = setup_my_download_dir('//Users//apple//thread_images')
    queue = Queue()
    links = list(chain(get_my_links(url1), get_my_links(url2), get_my_links(url3), get_my_links(url4), get_my_links(url5)))
    for x in range(8):
        worker = DownLoadMyWorker(queue)
        worker.daemon = True
        worker.start()
       
       
    for link in links:
        queue.put((download_dir, link)) 
    queue.join() 
    ts2 = time()
    ts = ts2 - ts1
    print ts   
