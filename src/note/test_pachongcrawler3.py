# -*- coding:utf-8 -*-
import urllib, urllib2
import time, random
import hashlib
headers = {
    'Referer':'http://fanyi.youdao.com/?keyfrom=dict2.index/',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    }
i = 'hello'
a = "rY0D^0'nM0}g5Mm1z%1G4"
n = 'fanyideskweb'
t = str(int(time.time()*1000) + random.randint(1,10))
print t
s = hashlib.md5(n + i + t + a).hexdigest()
print s
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
rq = urllib2.Request(url)
data = {}
data['i'] = 'hello'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
#data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = t
data['sign'] = s
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'

data2 = urllib.urlencode(data)
rq = urllib2.Request(url, data2, headers)
reponse = urllib2.urlopen(rq)
html = reponse.read()
print html