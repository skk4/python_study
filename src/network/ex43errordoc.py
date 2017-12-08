'''
Created on 2017.7.21

@author: Administrator
'''
import sys, urllib2
url = raw_input(">")
req = urllib2.Request(url)
try:
    fd = urllib2.urlopen(req)
    
except urllib2.HTTPError, e:
    print"Error retrieving data:" ,e
    print "Server error document follows:\n"
    print e.read()
    sys.exit(1)
except urllib2.URLError, e:
    print "Error retrieving data:", e
    sys.exit(2)
print "Retrieved " , fd.geturl()
for key, value in fd.info().items():
    print "%s = %s" %(key, value)   