# -*- coding:utf-8 -*-
import codecs
from pyecharts import Graph
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
node_dict = {}
node_list =[]
#node_time_list = []
edge_dict = {} 
edge_list = []
#读取txt节点文件
with codecs.open('sans_node_list.txt', 'r', 'utf-8') as f:
    for each_line in f:
        (node, time) = each_line.split()
        #print node, time
        node_dict[node] = int((int(time)+100)/10)
        node_list.append(node)
        #node_time_list.append((int(time)))               
#print node_time_list 
#读取边
with codecs.open('sans_edge_list.txt', 'r', 'utf-8') as f:
    for each_line in f:
        #print tuple(each_line.split())
        edge_list.append({'source':each_line.split()[0], 'target':each_line.split()[1]})

nodelist = []
print node_dict
for i in node_dict:
    nodelist.append({'name':i, 'category': i})
categories = nodelist
    
print edge_list 
graph = Graph("关系图-环形布局示例", width=1200, height=600)
graph.add("", nodelist, edge_list, categories, is_label_show=True, graph_repulsion=50,
               label_text_color=None, line_curve=0.2, label_pos="right")
graph.render('graph2.html')  
     