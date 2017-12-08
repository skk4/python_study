# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = pd.DataFrame(np.ones((3,3)), columns = ['A', 'B', 'C'])
x['D'] = x['A'] + x['B'] + x['C']
print x
sumrow_x =  x[['A', 'B', 'C', 'D']].sum()
print sumrow_x

x_sum = pd.DataFrame(data=sumrow_x).T
print x_sum
df_x_sum = x.append(x_sum, ignore_index=True)
print df_x_sum
print df_x_sum.describe()
print df_x_sum['A'].mean()
df_x_sum.plot()

#df_x_sum.plot(kind = 'bar', color ='m', alpha = 0.5, grid=True, title = 'good day')
plt.show()



