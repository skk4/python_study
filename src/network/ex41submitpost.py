# -*- coding:utf-8 -*-
'''
Created on 2017年7月21日

@author: Administrator
'''

'''
Created on 2017.7.21

@author: Administrator
'''
import sys, urllib2, urllib
zipcode = raw_input(">")
url = 'http://www.wunderground.com/cgi-bin/findweather/getForecast'
data = urllib.urlencode([('query', zipcode)]) 
print data   
print "Using URL", url
req = urllib2.Request(url, data)
try:
    fd = urllib2.urlopen(req)
    #print fd.geturl()
    print 'fd-----------------', fd.read()
except urllib2.HTTPError, e:
    print e.code
    print e.read()
    sys.exit(1) 


while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)
    
    