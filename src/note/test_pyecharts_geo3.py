# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Geo, Style
import codecs,json
import numpy as np
with codecs.open('weibo_geo.json', 'r', 'utf-8') as f:
    j  = json.load(f)


#print j[0]
#print j[1]
#print j[2]
coords ={}
i = 0
for x in j:   
    for y in x:
        coords[i] = y['geoCoord']
        i = i+1   
#print len(coords) 
subkey = np.arange(500)
subdict_attr=dict([(key, coords[key]) for key in subkey])
#print subdict_attr  
subdict_value = np.linspace(1, 1, 500)
#print list(subdict_value)     
coords_attr = np.arange(len(coords))
#print list(coords_attr)
coords_value = np.linspace(1, 1, len(coords))
#print list(coords_value)

style = Style(
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color='#404a59',

    )

geo = Geo(**style.init_style)
geo.add("weibo_light", coords_attr, coords_value, geo_cities_coords=coords, maptype="china", type = 'effectScatter', symbol_size = 1,is_roam = True,is_random= True)
geo.render('weibo_light.html')
print 'ok'

