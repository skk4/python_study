# -*- coding:utf-8 -*-
'''
Created on 2017年7月26日

@author: Administrator
'''
import urllib2, sys
request =  urllib2.Request('http://www.yoya.com')
response = urllib2.urlopen(request)

while 1:
    data = response.read(4096)
    if not len(data):
        break
    sys.stdout.write(data)
    
    info = response.info()
    if not len(info):
        break
    print '''----------'''
    #sys.stdout.write(str(info))
    print info