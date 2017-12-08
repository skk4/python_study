# -*- coding:utf-8 -*-
import pandas as pd
#数据及索引
a= [1, 5, 7, 9]
b = {'siming':1, 'huli':2, 'tongan':3, 'haicang':3}
c = ['1', '2', '3', '3']
#通过一维数组创建
pd_a = pd.Series(a)
#通过字典的方式创建
pd_b = pd.Series(b)
pd_c = pd.Series(c, index=['siming', 'huli', 'tongan', 'haicang'])
print pd_a
print pd_b
print pd_c
print pd_c['siming']
print pd_c['siming']
#单个赋值
pd_c['siming'] =7
#多个赋值
pd_c[['siming', 'huli']] = 7
print 'pd_c:\n', pd_c

#获取索引值
pd_c_index = pd_c.index
print pd_c_index
pd_c_values = pd_c.values
print pd_c_values
print list(set(pd_c_values))
print pd_c*2