# -*- coding:utf-8 -*-
import numpy as np
x = np.array([[1, 3, 5], [2, 4, 6]])
print x
#获取第2行,第3列
print x[1, 2]
#获取第2行所以元素
print x[1,:]

#获取第2行，第2到第3元
print x[1, 1:3]

#赋值
x[1, :] = [6, 6, 8]
print x[1, :]
print x

for each_x in x:
    print 'each_x:', each_x
    
y = np.linspace(1, 5, 4)
for each_y in y:
    print 'each_y:', each_y    


