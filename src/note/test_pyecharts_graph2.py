# -*- coding:utf-8 -*-
import codecs
import json
from pyecharts import Graph
with codecs.open('weibo.json', 'r', 'utf-8') as f:
    j = json.load(f)
    
    
#print j 
#print len(j)
nodes, links, categories, cont, mid, _ = j

print nodes
nodes_list = []

for m in nodes:
    #print m
    for n in m:
        pass
        #print n
    #print m['name']
    nodes_list.append({'name':m['name'], 'symbolSize':m['symbolSize'], 
                       'category':m['category']})
#print nodes_list    
print categories           
'''
print len(categories)
for x in categories:
    print 'x',x
    for y in x:
        print '%s---%s' %(y, x[y])
        
'''        
graph = Graph("微博转发关系图", width=1200, height=600)
graph.add("", nodes_list, links, categories, label_pos="right",
              graph_repulsion=50, is_legend_show=False,
              line_curve=0.2, label_text_color=None, is_label_show=True)
graph.render('graph3.html')        