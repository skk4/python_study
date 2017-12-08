# -*- coding:utf-8 =*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])  
print df2 
df2.plot(kind='bar')  #分开并列线束  
df2.plot(kind='bar', stacked=True) #四个在同一个里面显示 百分比的形式  
df2.plot(kind='barh', stacked=True)#纵向显示  
plt.show() 
'''

df4=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000)-1},columns=list('abc'))  
df4.plot(kind='hist', alpha=0.5)  
df4.plot(kind='hist', stacked=True, bins=20)  
df4['a'].plot(kind='hist', orientation='horizontal',cumulative=True) #cumulative是按顺序排序，加上这个  
plt.show()  