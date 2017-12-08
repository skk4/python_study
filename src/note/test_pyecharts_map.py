# -*- coding:utf-8 -*-
from pyecharts import Map
from pyecharts import Style
from pyecharts import Geo
style = Style(
        width=1100, height=600
    )
provinces =[('福建', 20), ('广东', 70), ('北京', 100), ('重庆', 65),
            ('天津', 95), ('山东', 80), ('新疆', 50), ('湖北', 77),
            ('香港', 66), ('云南', 40), ('四川', 62), ('甘肃', 100),
            ('西藏', 33)]

map = Map('china-map', **style.init_style)
    
attr = [each_pv[0] for each_pv in provinces]  
value =  [each_pv[1] for each_pv in provinces]
map.add('', attr, value, maptype='china', is_label_show = True , is_visualmap = True, visual_text_color='#000')
map.render('map.html')