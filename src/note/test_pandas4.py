# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
#通过[]二维数组生成数据
print np.ones((2,2))
x = pd.DataFrame(np.ones((2,2)),columns=['A', 'B'])
print x
print "x['A']:\n"
print x['A']
print "x.A:\n"
print x.A
print "x.A.values:\n"
print x.A.values
print 'list(set(x.A.values))'
print list(set(x.A.values))
print list(x.A.index)

print '-----'
x[['A', 'B']] = 2
print x

print x[['A', 'B']].sum()

#通过字典生成数据
y_dict = {'A':[1, 2, 3], 'B':[4, 5, 6], 'c':[7, 8, 9]}
y = pd.DataFrame(y_dict)
print y


