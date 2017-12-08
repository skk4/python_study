# -*- coding:utf-8 -*-
#关系图
import networkx as nx
import matplotlib.pyplot as plt
dg = nx.DiGraph()#空有向关系图
#dg = nx.Graph()#空无向关系图
nodes = ['A', 'B', 'C', 'D', 'E']
relation1 = ['B', 'C', 'D', 'E', 'A']
relation2 = ['c', 'D']
#添加节点列表
dg.add_nodes_from(nodes)  
ebunch1 = zip(nodes, relation1)
ebunch2 = zip(nodes, relation2)  
#添加边有方向,数据格式为列表
dg.add_edges_from(ebunch1)
dg.add_edges_from(ebunch2)
#各节点大小列表
sizes = [300, 900, 450, 600, 750]
colors = ['green', 'red', 'blue', 'yellow', 'gray']
print dg.number_of_edges()#获取边的总数
print dg.edges()
#各边颜色列表
edge_colors = ['green', 'red', 'blue', 'yellow', 'gray', 'k', 'm']
#pos = nx.circular_layout(dg)
#pos = nx.shell_layout(dg)
#pos = nx.spring_layout(dg)
pos = nx.spectral_layout(dg)
#各边宽度列表
widths = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]

#设置属性
dg.node['A']['money']= 1000
dg.nodes(data=True)
print dg.node['A']['money'] 
dg['A']['B']['weight'] = 12.0
print dg['A']['B']['weight']

# style='dashed' 表示虚线
nx.draw(dg, pos =pos , with_labels = True, node_size=sizes, node_color = colors, edge_color = edge_colors,
         width= widths, style='dashed')
#nx.draw_networkx(dg, with_labels = True, node_size=sizes, node_color = colors, edge_color = edge_colors)
plt.show()
