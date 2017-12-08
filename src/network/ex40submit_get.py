'''
Created on 2017.7.21

@author: Administrator
'''
import sys, urllib2, urllib


def addgetdata(url, data):
    '''Adds data to url. Data should be a list or tuple consisting of 2-item 
    lists or tuples of the form :(key, value)
    
    Items that have no key should key set to None.
    
    A given key may occur more than once.'''
    
    return url + '?' + urllib.urlencode(data, doseq = 0)

zipcode = raw_input(">")
#words = 'python'
#max = 25
#source = 'www'

url = addgetdata('http://www.wunderground.com/cgi-bin/findweather/getForecast', [('query', zipcode)])
#url = addgetdata('http://www.freebsd.org/cgi/search.cgi', [('words', zipcode)])
#url = addgetdata('http://www.freebsd.org/cgi/search.cgi', [('words', words), ('max', max), ('source',source)])
    
print "Using URL", url
req = urllib2.Request(url)
fd = urllib2.urlopen(req)
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)    