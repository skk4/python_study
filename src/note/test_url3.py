# -*- coding:utf-8 -*-
import  urllib2
req = urllib2.Request("http://www.unicode.org/mail-arch/")
fd = urllib2.urlopen(req)
print fd.info()