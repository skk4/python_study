# -*- coding:utf-8 -*-
#爬虫
import urllib2, urllib
content = raw_input("输入翻译的文字：")
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['client'] = 'fanyideskweb'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'
data['smartresult'] = 'dict'
data['salt'] = '1504861503043'
data['sign'] = '8496cea4103963e00079953e0e8b0478'
newdata = urllib.urlencode(data)
print newdata
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
request = urllib2.Request(url)
#request = urllib2.Request(url, newdata, headers)
#fd = urllib2.urlopen(request)
#request.add_header('User-Agent', 'fake-client')
fd = urllib2.urlopen(request, newdata)
print fd.info()
html = fd.read()
print html

