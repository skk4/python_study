# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
'''
#直方图
mu = 100
sigma = 20
x = mu + sigma*np.random.randn(20000)
plt.hist(x, bins=100, color='green', normed=True)
plt.show()
'''

#条形图
y = [20, 10, 30, 25, 15]
index = np.arange(5)
plt.bar(left=index, height=y, color='green', width=0.5)
plt.show()

'''
#饼状图
labels = 'A', 'B', 'C', 'D'
#print type(labels)
fracs = [15, 30, 45, 10]
plt.axes(aspect = 1)#使x y轴比例相同
explode = [0, 0.1, 0, 0]# 突出某一部分区域
plt.pie(x=fracs, labels=labels, autopct='%.0f%%', explode=explode)#autopct显示百分比
plt.show()
'''

#折线图
x = np.linspace(-10, 10, 100)
y = x**3
plt.plot(x, y, linestyle='--', color='green', marker='<')
plt.show()

'''
#散点图
x = np.random.randn(1000)
y = x + np.random.randn(1000)*0.5
plt.scatter(x, y, s=5, marker='<')# s表示面积，marker表示图形
plt.show()
'''