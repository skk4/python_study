# -*- coding:utf-8 -*-
'''
Created on 2017.7.20

@author: Administrator
'''
import urllib2, sys
hostname =  raw_input(">")
req = urllib2.Request(hostname)
fd = urllib2.urlopen(req)
while 1:
    data = fd.read(8192)
    if not len(data):
        break
    sys.stdout.write(data)