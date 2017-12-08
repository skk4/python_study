# -*- coding:utf-8 -*-
import  urllib2
req = urllib2.Request("http://www.fishc.com")
fd = urllib2.urlopen(req)
html = fd.read()
print html