# -*- coding:utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import codecs
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
node_dict = {}
node_list =[]
#node_time_list = []
edge_dict = {} 
edge_list = []
#txt中获取节点，及节点出现次数
with codecs.open('sans_node_list.txt', 'r', 'utf-8') as f:
    for each_line in f:
        (node, time) = each_line.split()
        #print node, time
        node_dict[node] = int(time)
        node_list.append(node)
        #node_time_list.append((int(time)))               
#print node_time_list 
#获取边，及边出现的次数
with codecs.open('sans_edge_list.txt', 'r', 'utf-8') as f:
    for each_line in f:
        #print tuple(each_line.split())
        edge_list.append(tuple(each_line.split()))
        
#print edge_list  

G=nx.Graph()
G.add_nodes_from(node_list)

new_node_time_list = []
G.nodes()
for z in G.nodes():
    new_node_time_list.append((int(node_dict[z])+300))
print new_node_time_list 

#批量增加带权边
G.add_weighted_edges_from(edge_list)
#按权重划分为重权值得边和轻权值的边
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) >100]
print elarge
emiddle=[(u,v) for (u,v,d) in G.edges(data=True) if 50< int(d['weight']) <=100] 
print emiddle
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if int(d['weight']) <=50]
print esmall
#节点位置
#pos=nx.spring_layout(G)
#pos = nx.circular_layout(G)
#pos = nx.shell_layout(G)
pos = nx.random_layout(G)
#pos = nx.spectral_layout(G)
#首先画出节点位置
   
nx.draw_networkx_nodes(G, pos, node_size=new_node_time_list)


#画边
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=8, edge_color='r')
nx.draw_networkx_edges(G,pos,edgelist=emiddle,
                    width=4,alpha=0.5,edge_color='m')
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=1,alpha=0.5,edge_color='b' )

# labels标签定义
#nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

nx.draw_networkx_labels(G,pos,font_size=10)
plt.axis('off')#去掉坐标
plt.savefig("weighted_graph2.png") # save as png
plt.show() # display