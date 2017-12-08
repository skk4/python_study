# -*- coding:utf-8 -*-
import  urllib2 
req = urllib2.Request("http://placekitten.com/g/500/600")
fd = urllib2.urlopen(req)
cat_image = fd.read()
#print cat_image

with open('cat_500_600.jpg', 'wb') as f:
    f.write(cat_image)    
    
    
print fd.geturl() 
print fd.info() 
print fd.getcode()  