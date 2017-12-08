# -*- coding:utf-8 -*-
import numpy as np
a = [1, 4, 6, 8, 10]
b = (1, 1.2, 2.1, 3)
c1 = [1, 2, 3]
c2 = [3, 7, 9]
c3 = [6, 9, 2]
d =  [1, 2]
'''
#np.array方法，生成[1 4 6 8 10],或者
[[1 2 3] 
 [3 7 9] 
 [6 9 2]]
'''
np_a = np.array(a)
np_b = np.array(b)
np_c = np.array([c1, c2, c3], dtype = np.int64)
print '--------'

print np_a
print np_b
print np_b.ndim
print np_c
print type(np_a)
print type(np_b)
print type(np_c)
print np_c.ndim
print np_c.dtype

#np.arange()方法,生成[ 1  3  5  7  9 11]
np_x = np.arange(1, 12, 2)
print np_x
#np.reshape(3, 2), 拆成3行2列
np_x_shape = np_x.reshape(3, 2)
print '----', np_x_shape
print '----', np_x_shape.ndim
print '----', np_x_shape.shape

#np.linspace(1,2,5),从1~2中拆成5等分
np_y = np.linspace(1, 2, 5)
print np_y
'''
#np.zero 
[[ 0.  0.]
 [ 0.  0.]
 [ 0.  0.]]
'''
np_z = np.zeros((3, 2))
print np_z

'''
#np.ones
[[ 1.  1.]
 [ 1.  1.]
 [ 1.  1.]]
'''
np_o = np.ones((3, 2))
print np_o


'''
#np.eye
[[ 1.  0.  0.  0.]
 [ 0.  1.  0.  0.]
 [ 0.  0.  1.  0.]
 [ 0.  0.  0.  1.]]
'''
np_e = np.eye(4)
print np_e

'''
三维数组
维数、shape值、元素个数、元素字节数
'''
np_n = np.zeros((3,2,4))
print np_n
print np_n.ndim
print np_n.shape
print np_n.size
print np_n.itemsize

np_mgrid = np.mgrid[0:5, 0:5]
print np_mgrid

np_random = np.random.rand(5, 5)
print np_random
