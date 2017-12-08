# -*- coding:utf-8 -*-
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
#单个列值
data['A']
print  data
#多列赋值
data[['A', 'B', 'C', 'D']]= 3
print data
#新增列
data['E']= 4
print data