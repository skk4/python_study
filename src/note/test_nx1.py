# -*- coding:utf-8 -*-
#关系图
import networkx as nx
import matplotlib.pyplot as plt
dg = nx.DiGraph()
#添加单节点
dg.add_node('A', node_size = 700 , node_color = 'green')
#添加一个节点
dg.add_node('B')
#添加边有方向
dg.add_edge('A', 'B')
nx.draw(dg, with_labels = True, node_size=[300, 900], node_color = ['green', 'red'])
plt.show()

