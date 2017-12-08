# -*- coding:utf-8 -*-
import urllib , urllib2, json, codecs
#正逆地理坐标编码
#百度AK
ak = 'moR7z2ykhST1BmqWIa66S7yUQGGPpKhI'
output = 'json'
city = '厦门'
address_list = ['中山路']
address_geos = []
for address in address_list:
    add = urllib.quote(address)
    city= urllib.quote(city)
    #print add
    url = 'http://api.map.baidu.com/geocoder/v2/'
    uri = url + '?' + 'address=' + add + 'city=' + city+ '&output=' + output + '&ak=' + ak
    rq = urllib2.Request(uri)
    fq = urllib2.urlopen(rq)
    res = fq.read()
    point_json = json.loads(res)
    address_geos.append(point_json['result']['location'])
print address_geos    

