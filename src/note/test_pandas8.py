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
data_2 = pd.DataFrame(data[data>2])
#批量修改nan值
print data_2
x = data_2.fillna(value=6)
print x

#删除nan行数据
print data[data>2].dropna(how='any')


#填补缺失项
print 'ha------------ha'
print x.reindex(index=list(x.index)+['seven'],columns=list(x.columns)+['E'])

print 'ha------------ha'
print x.reindex(index=['one','six'],columns=list(x.columns)+['E'])



