# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#设置字体，选中中文字体地址
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttf', size=9)
x = np.arange(1, 8)
y = np.array([50000, 45000, 25000, 32000, 30000, 27000, 13000])
group_labels = [u'思明区', u'湖里区', u'同安区', u'海沧区', u'集美区', u'翔安区', u'漳州']
#fontproperties设置字体
plt.title(u'丹夏房产', fontproperties=zhfont1)
plt.xlabel(u'厦门各区', fontproperties=zhfont1)
plt.ylabel(u'平均房价', fontproperties=zhfont1)
plt.bar(left=x, height=y, width=0.1, color='c', yerr = 0.01, align ='center', alpha=0.8)
plt.plot(x,y, color = 'm', marker='x')
plt.xticks(x, group_labels, rotation=10, fontproperties=zhfont1)
print 'zip', zip(x, y)
for a,b in zip(x,y):
    print 'a:%s , b:%s' %(a, b)
    
    
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
plt.grid()
#prop设置图例字体
plt.legend(['各区房价折线图'.decode('utf-8'), '各区房价柱状图'.decode('utf-8')],prop=zhfont1)
#plt.savefig('house.jpg')
plt.show()