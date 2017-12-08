# -*- coding:utf-8 -*-
import urllib
import urllib2
import json
while 1:
    content = raw_input(">:")
    headers = {
        'Referer': 'http://fanyi.baidu.com/?aldtype=16047/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        }
    
    
    data = {}
    data['from'] = 'en'
    data['to'] = 'zh'
    data['query'] = content
    data['transtype'] = 'translang'
    data['simple_means_flag'] = '3'
    url = 'http://fanyi.baidu.com/v2transapi'
    values = urllib.urlencode(data)
    rq = urllib2.Request(url, values, headers)
    fd = urllib2.urlopen(rq)
    #print fd.getcode()
    html = fd.read()
    #print html
    #print html
    dst = json.loads(html)
    print dst['trans_result']['data'][0]['dst']

