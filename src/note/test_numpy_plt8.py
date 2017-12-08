# -*- coding:utf-8 =*-
from pylab import  *  
x=np.linspace(-np.pi,np.pi,256,endpoint=True)  
c,s=np.cos(x),np.sin(x)  
plot(x,c, color="blue", linewidth=2.5, linestyle="-", label="cosine")  #label用于标签显示问题  
plot(x,s,color="red",  linewidth=2.5, linestyle="-", label="sine")  
show()  


from numpy.random import random  
  
colors = ['b', 'c', 'y', 'm', 'r']  
  
lo = plt.scatter(random(10), random(10), marker='x', color=colors[0])  
ll = plt.scatter(random(10), random(10), marker='o', color=colors[0])  
l  = plt.scatter(random(10), random(10), marker='o', color=colors[1])  
a  = plt.scatter(random(10), random(10), marker='o', color=colors[2])  
h  = plt.scatter(random(10), random(10), marker='o', color=colors[3])  
hh = plt.scatter(random(10), random(10), marker='o', color=colors[4])  
ho = plt.scatter(random(10), random(10), marker='x', color=colors[4])  
  
plt.legend((lo, ll, l, a, h, hh, ho),  
           ('Low Outlier', 'LoLo', 'Lo', 'Average', 'Hi', 'HiHi', 'High Outlier'),  
           scatterpoints=1,  
           loc='lower left',  
           ncol=3,  
           fontsize=8)  
  
plt.show()  