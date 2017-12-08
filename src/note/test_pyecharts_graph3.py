# -*- coding:utf-8 -*-
from pyecharts import Graph
'''
nodes = [
    {"name": "结点1", "symbolSize": 10},
    {"name": "结点2", "symbolSize": 20},
    {"name": "结点3", "symbolSize": 30},
    {"name": "结点4", "symbolSize": 40},
    {"name": "结点5", "symbolSize": 50},
    {"name": "结点6", "symbolSize": 40},
    {"name": "结点7", "symbolSize": 30},
    {"name": "结点8", "symbolSize": 20}]
'''
nodes = [
    {"name": "结点1"},
    {"name": "结点2"},
    {"name": "结点3"},
    {"name": "结点4"},
    {"name": "结点5"},
    {"name": "结点6"},
    {"name": "结点7"},
    {"name": "结点8"}]   
    



links = []
for i in nodes:
    #print 'i----',i
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})
        
for x1 in links:
    print 'x'
    for x2 in x1:
        print '%s ---- %s' %(x2,x1[x2])        
     
graph = Graph("关系图-环形布局示例")
graph.add("", nodes, links, is_label_show=True, graph_repulsion=8000,
               label_text_color=None)
graph.render('graph.html') 
print 'ok'       