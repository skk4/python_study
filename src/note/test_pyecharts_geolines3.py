# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import codecs
import json
from pyecharts import GeoLines, Style


style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1800,
    height=1200,
    background_color="#404a59"
)

style_geo = style.add(
    is_label_show=False,
    line_curve=0.2,
    line_opacity=0.6,
    #line_color = 'gray',
    line_color = 'rgba(100,149,237,0.2)',
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="pin",
    geo_effect_symbolsize=1,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
    symbol = 'circle',
    symbol_size  = 1,
    legend_selectedmode="multiple",
    geo_effect_period = 10,
)


with codecs.open('migration.json', 'r', 'utf-8') as f:
    j  = json.load(f)
#print j
for m in j:
    '''
    for n in j['topCityIn']:
        print n['name']
    print '------split------'    
    for n in j['topCityOut']:
        print n['name']
        
    print '------split------'
    for n in j['topLine']:
        print '%s-%s' %(n['start'], n['end'])  
        
'''        
    print '------split------'
    data_allline = []
    for n in j['allLine']:
        pass
        data_allline.append([n['start'].split('_')[1], n['end'].split('_')[1]])    
data_allline

data_beijingout = []
for x in data_allline:
    if x[0]== u'北京':
        data_beijingout.append([x[0], x[1]])
 
data_beijingin = []
for x in data_allline:
    if x[1]== u'北京':
        data_beijingin.append([x[0], x[1]])


data_shanghaiout = []
for x in data_allline:
    if x[0]== u'上海':
        data_shanghaiout.append([x[0], x[1]])
        
data_shanghaiin = []
for x in data_allline:
    if x[1]== u'上海':
        data_shanghaiin.append([x[0], x[1]])
        
data_guangzhouout = []
for x in data_allline:
    if x[0]== u'广州':
        data_guangzhouout.append([x[0], x[1]])
data_guangzhouin = []
for x in data_allline:
    if x[1]== u'广州':
        data_guangzhouin.append([x[0], x[1]])
        

lines = GeoLines("人口迁徙模拟示例", **style.init_style)
lines.add("", data_allline, **style_geo)
lines.show_config()
lines.render('migration.html') 
print 'ok'  
           