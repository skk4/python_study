# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
group_labels = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'June.', 'July.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
columns = ['siming', 'huli', 'tongan', 'haicang', 'jimei', 'xiangan']
house_jan = [53297,45869, 20358, 32550, 29359, 19270]
house_feb = [53297,45869, 20358, 32550, 29359, 19270]
house_mar = [53297,45869, 20358, 32550, 29359, 19270]
house_apr = [53297,45869, 20358, 32550, 29359, 19270]
house_may = [53297,45869, 20358, 32550, 29359, 19270]
house_june = [53297,45869, 20358, 32550, 29359, 19270]
house_july = [53297,45869, 20358, 32550, 29359, 19270]
house_agu = [53297,45869, 20358, 32550, 29359, 19270]
house_sept = [53297,45869, 20358, 32550, 29359, 19270]
house_oct = [53297,45869, 20358, 32550, 29359, 19270]
house_nov = [53297,45869, 20358, 32550, 29359, 19270]
house_dec = [53297,45869, 20358, 32550, 29359, 19270]

house_list = np.array([house_jan, house_feb, house_mar, house_apr, house_may, house_june,
                      house_july, house_agu, house_sept, house_oct, house_nov, house_dec])
print house_list
df = pd.DataFrame(house_list, columns= columns)
x = list(df.index)
y1 = list(df['siming'])
y2 = list(df['huli'])

df.plot(kind = 'bar', grid = True, yerr = 0.0005, figsize=(12, 6))
#获取数据标签
df_columns = list(df.columns)#df数据列
columns_number = len(df_columns)#数据列个数
for i in range(columns_number):
    columns_values  = list(df[df_columns[i]])#遍历各数据列的值
    for a , b in zip(x, columns_values):
        plt.text(a+0.1, b+0.1, '%.0f' % b, ha='center', va= 'bottom',fontsize=15, color = 'red')#标注各数据标签值
plt.xticks(x, group_labels, rotation=10)
plt.legend(loc=1, numpoints=1, fontsize=7)
#df.plot(kind = 'bar', grid = True, stacked=True)
'''
df.plot(kind = 'bar', grid = True, yerr = 0.0005)

for a,b in zip(x,y1):
    plt.text(a, b+0.1, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    
for a,b in zip(x,y2):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)   
    
'''     
#df.plot(kind='area')  
#df.plot(kind='area',stacked=False)
#df.plot(kind='scatter', x='siming', y='huli')  
#df.plot(kind='scatter', x='siming', y='huli',color='DarkBlue', label='Group 1')  
#df.plot(kind = 'pie', subplots=True)
#plt.xticks(x, group_labels, rotation=10)
#plt.text(1, 40000, 'hello')
plt.show()


