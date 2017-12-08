# -*- coding:utf-8 -*-
#import socket
import random
import urllib2
iplist = ['111.13.7.42:81']
url = 'http://www.whatismyip.com.tw/'
proxy = {'http': random.choice(iplist)}
proxy_support = urllib2.ProxyHandler(proxy)
opener = urllib2.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')]
urllib2.install_opener(opener)
rq = urllib2.Request(url)

print rq.get_full_url()
fd = urllib2.urlopen(rq)
print fd.read()
fd.close()
