# -*- coding:utf-8 -*-
import pandas as pd 
data=pd.DataFrame([[1,1,1,1],[1,1,1,1],[2,1,4,3],[5,6,7,9],[5,4,2,1],[2,1,4,9]],columns=['A','B','C','D'])
#print data
'''
   A  B  C  D
0  1  1  1  1
1  1  1  1  1
2  2  1  4  3
3  5  6  7  9
4  5  4  2  1
5  2  1  4  9

'''
# head()、 tail()
print data.head()#显示前5行数据，data.head(n = 3)显示前3行数据
print data.tail()#显示后5行数据，data.tail(n = 3)显示后3行数据

# index、values、columns,显示索引、数值、标签
print data.index
print data.values
print data.columns

# describe()，对每一列数据进行统计，包括计数、最大值、最小值、平均值、std、分位数等
print data.describe()

# T 数据转置,对data_sum数据进行转置
data_sum  = pd.DataFrame(data[['A', 'B', 'C', 'D']].sum())
print data_sum.T

# 对轴进行排序
print data
print '--------------'
print data.sort_index(axis=1, ascending=0)# 对标签ABCD进行降序
print '--------------'
print data.sort_index(axis=0, ascending=0)# 对索引进行降序
print '--------------'
print data.sort_values(by=['A', 'B'], ascending=[0, 1])# 对数值进行排序
