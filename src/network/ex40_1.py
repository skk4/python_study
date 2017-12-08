# -*- coding:utf-8 -*-
'''
Created on 2017年7月26日

@author: Administrator
'''
import urllib2, urllib

data =[('query','10001')]
url = 'http://www.wunderground.com/cgi-bin/findweather/getForecast'+ '?' + urllib.urlencode(data)
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()