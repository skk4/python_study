# -*- coding:utf-8 -*-
import random
import urllib2
iplists = ['120.32.139.155:2745']
#61.135.217.7,119.55.136.97,120.32.139.155:27458

proxy = {'http': random.choice(iplists)}
proxy_support = urllib2.ProxyHandler(proxy)
opener = urllib2.build_opener(proxy_support)
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
urllib2.install_opener(opener)
url = 'http://www.whatismyip.com.tw'
rq = urllib2.Request(url)
#rq = urllib2.Request(url, headers=headers)
fd = urllib2.urlopen(rq)
html = fd.read()
print 'html', html
fd.close()