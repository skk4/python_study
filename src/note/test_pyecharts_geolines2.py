# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from pyecharts import GeoLines, Style


style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#404a59"
)

style_geo = style.add(
    is_label_show=False,
    line_curve=0.2,
    line_opacity=0.5,
    line_color = 'rgba(100,149,237,0.2)',
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="circle",
    geo_effect_symbolsize=1.5,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
    symbol = 'pin',
    symbol_size  = 1,
    legend_selectedmode="multiple",
    is_roam = True,
    geo_effect_period = 1,
    is_symbol_show = True,
    is_map_symbol_show = True,
    is_random = False,
)


def test_geolines():
    data_bazong = [
        ['北京', '哈尔滨'],
        ['哈尔滨', '满洲里'],
        ['沈阳', '大连'],
        ['大连', '烟台'],
        ['烟台', '青岛'],
        ['青岛', '淮安'],
        ['淮安', '上海'],
        ['上海', '杭州'],
        ['杭州', '宁波'],
        ['宁波', '温州'],
        ['温州', '福州'],
        ['福州', '厦门'],
        ['厦门', '广州'],
        ['广州', '湛江'],
        ['北京', '天津'],
        ['天津', '济南'],
        ['济南', '南京'],
        ['南京', '上海'],
        ['北京', '南昌'],
        ['南昌', '深圳'],
        ['深圳', '九龙红磡'],
        ['北京', '郑州'],
        ['郑州', '武汉'],
        ['武汉', '广州'],
        ['大同', '太原'],
        ['太原', '焦作'],
        ['焦作', '洛阳'],
        ['洛阳', '柳州'],
        ['柳州', '湛江'],
        ['包头', '西安'],
        ['西安', '重庆'],
        ['重庆', '贵阳'],
        ['贵阳', '柳州'],
        ['柳州', '南宁'],
        ['兰州', '成都'],
        ['成都', '昆明']
        
    ]
    data_baheng = [
        ['北京', '兰州'],
        ['兰州', '拉萨'],
        ['大同', '秦皇岛'],
        ['神木', '黄骅'],
        ['太原', '德州'],
        ['德州', '龙口'],
        ['龙口', '烟台'],
        ['太原', '德州'],
        ['德州', '济南'],
        ['济南', '青岛'],
        ['长治', '邯郸'],
        ['邯郸', '济南'],
        ['济南', '青岛'],
        ['瓦塘', '临汾'],
        ['临汾', '长治'],
        ['长治', '汤阴'],
        ['汤阴', '台前'],
        ['台前', '兖州'],
        ['兖州', '日照'],
        ['侯马', '月山'],
        ['月山', '新乡'],
        ['新乡', '兖州'],
        ['兖州', '日照'],
        ['连云港', '郑州'],
        ['郑州', '兰州'],
        ['兰州', '乌鲁木齐'],
        ['乌鲁木齐', '阿拉山口'],
        ['西安', '南阳'],
        ['南阳', '信阳'],
        ['信阳', '合肥'],
        ['合肥', '南京'],
        ['南京', '启东'],
        ['重庆', '武汉'],
        ['武汉', '九江'],
        ['九江', '铜陵'],
        ['铜陵', '南京'],
        ['南京', '上海'],
        ['上海', '怀化'],
        ['怀化', '重庆'],
        ['重庆', '成都'],
        ['成都', '贵阳'],
        ['贵阳', '昆明'],
        ['昆明', '南宁'],
        ['南宁', '黎塘'],
        ['黎塘', '湛江'],
        ["北京", "南京"],
        ["北京", "重庆"],    
    ]       
    lines = GeoLines("GeoLines 示例", **style.init_style)
    lines.add("八纵", data_bazong, **style_geo)
    lines.add("八横", data_baheng, **style_geo)
    lines.show_config()
    lines.render('geolines.html')
test_geolines()
print 'ok'