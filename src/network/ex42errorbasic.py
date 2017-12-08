'''
Created on 2017.7.21

@author: Administrator
'''
import sys, urllib2
url = raw_input(">")
req = urllib2.Request(url)
try:
    fd = urllib2.urlopen(req)
except urllib2.URLError, e:
    print 'Error retrieved data:', e
    sys.exit(1)

print "Retrieved" , fd.geturl()    
info = fd.info()
for key, value in info.items():
    print "%s = %s" %(key, value)