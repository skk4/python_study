# -*- coding:utf-8 -*-
'''
Created on 2017年7月26日

@author: Administrator
'''
import urllib
data = {'qurey':'10001','max':'25'}
print urllib.urlencode(data)

data2 = [('query','10001'),('max','25')]

print urllib.urlencode(data2)