# -*- coding:utf-8 -*-
import urllib , urllib2, json, codecs
#正逆地理坐标编码
#百度AK
ak = 'XdYffQBHlHsimyBCIRRu8GvEyAQPS8d4'
output = 'json'
addr_ip = '24.46040946447703,118.0876375459098'
url = 'http://api.map.baidu.com/geocoder/v2/'
uri = url + '?' + '&location=' + addr_ip +  '&output='+output +'&pois=1'+ '&ak=' + ak
rq = urllib2.Request(uri)
fq = urllib2.urlopen(rq)
res = fq.read()
point_json = json.loads(res)
print point_json['result']['formatted_address']