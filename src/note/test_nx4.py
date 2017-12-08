# -*- coding:utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

node_dict = {}
node_list =[]
node_time_list = []
edge_dict = {} 
edge_list = []
#txt中获取节点，及节点出现次数
with open('node_list.txt', 'r') as f:
    for each_line in f:
        (node, time) = each_line.split()
        node_dict[node] = int(time)
        node_list.append(node)
        node_time_list.append((int(time)+10)*30)
#print node_list
#print node_time_list               
#print node_dict 
#获取边，及边出现的次数
with open('edge_list.txt', 'r') as f:
    for each_line in f:
        #print tuple(each_line.split())
        edge_list.append(tuple(each_line.split()))
        
#print edge_list  

G=nx.Graph()
#批量增加带权边
G.add_weighted_edges_from(edge_list)
#按权重划分为重权值得边和轻权值的边
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) >50]
print elarge
emiddle=[(u,v) for (u,v,d) in G.edges(data=True) if 20< int(d['weight']) <=50] 
print emiddle
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) <=20]
print esmall
#节点位置
pos=nx.spring_layout(G)
#首先画出节点位置
#nx.draw_networkx_nodes(G,pos, node_size=node_time_list)
G.add_nodes_from(node_list, node_size = node_time_list)
#画边
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=10)
nx.draw_networkx_edges(G,pos,edgelist=emiddle,
                    width=8,alpha=0.5,edge_color='m')
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b')

'''
#加入带权边
G.add_edge('a','b',weight=0.6)
G.add_edge('a','c',weight=0.2)
G.add_edge('c','d',weight=0.1)
G.add_edge('c','e',weight=0.7)
G.add_edge('c','f',weight=0.9)
G.add_edge('a','d',weight=0.3)

#按权重划分为重权值得边和轻权值的边
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

G.add_weighted_edges_from([('a', 'b', 0.6), ('a', 'c', 0.2), 
                           ('c', 'd', 0.1), ('c', 'e', 0.7),
                           ('c', 'f', 0.9), ('a', 'd', 0.3)])
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
print d
print elarge
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]
print esmall
#节点位置
pos=nx.spring_layout(G) # positions for all nodes
#首先画出节点位置
# nodes
nx.draw_networkx_nodes(G,pos, node_size=[100, 200, 300, 400, 500, 600])
#依据权重，实线为权值大的边。虚线为权值小的边
# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=6)
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')
'''
# labels标签定义
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
plt.axis('off')#去掉坐标
plt.savefig("weighted_graph.png") # save as png
plt.show() # display