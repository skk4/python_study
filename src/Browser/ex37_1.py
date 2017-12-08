# -* - coding: UTF-8 -* -  
'''
Created on 2017年7月26日

@author: Administrator
'''

import urllib2

request = urllib2.Request("http://www.yoya.com/")
#request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
print "----------------------",response.getcode()
print response.geturl()
print response.read()
print response.info()