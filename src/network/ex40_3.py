# -*- coding:utf-8 -*-
'''
Created on 2017年7月26日

@author: Administrator
'''
import urllib
import urllib2

values = {"username":"skk_4@163.com","password":"skk_1983xie"}
data = urllib.urlencode(values) 
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()