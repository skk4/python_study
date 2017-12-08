# -*-coding:utf-8 -*-
import urllib2
import json
import time
'''
import json
a = '{"totalPage":100,"curPage":1}'
b = json.loads(a)
print b
print b['totalPage']
print type(b)
'''
#url = 'http://xm.lianjia.com/ershoufang/105101004155.html'

def open_url():
    url = 'http://xm.lianjia.com/ershoufang/siming'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    rq = urllib2.Request(url, headers=headers)
    fd = urllib2.urlopen(rq)
    html = fd.read()

for i in range(1, 4):
    url_page = 'https://xm.lianjia.com/ershoufang/siming/' + 'pg'+ str(i) + '/'
    open_url(url_page)   