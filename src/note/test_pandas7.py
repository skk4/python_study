# -*-coding:utf-8 -*-
import pandas as pd 
data=pd.DataFrame([[1,1,1,1],[1,1,1,1],[2,1,4,3],[5,6,7,9],[5,4,2,1],[2,1,4,9]],
                  index= ['one', 'two', 'three', 'four', 'five', 'six'], columns=['A','B','C','D'])
'''
       A  B  C  D
one    1  1  1  1
two    1  1  1  1
three  2  1  4  3
four   5  6  7  9
five   5  4  2  1
six    2  1  4  9

'''
print data
#选择标签返回列，单个列
print data['A']
#选择标签返回列，多个列
print data[['A', 'B', 'C']]
print '------------'
#选择索引位置号，返回行，3到4行
print data[2:4]
print '------------'
#选择索引位置号和标签值，返回指定行和列
print data.ix[1:2,["A", "B"]]
print 'ixxxxxxx'
print data.ix[[0, 1, 2],['A', 'B', 'C']]
print "xxxxiiiiii"
print data.ix[[0, 1, 2],[0, 1, 2]]
print '------------'
#选择索引和标签的具体值，返回指定行
print data.loc['three']
print '------------'
print data.loc[['one','two'],['A', 'B']]
print '------------'
#选择行列进行切片
print data.iloc[0:3, 0:3]
#自由选择行列位置
print data.iloc[[0,3],[0,3]]
print '--------- dataA'
print data[data.A>2]
print '--------- A'
print data[data>2]
print '----------'
#



