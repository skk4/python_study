# -*- coding:utf-8 -*-
import numpy as np
x = np.zeros((2, 4))
y = np.ones((2, 4))
z = np.eye(2,4)
print x
print y
print z
print x+y
print x-y

y2 = y*2
z2 = z*2
print 'y2:\n', y2
print 'z2:\n', z2
print 'y2*z2:\n', y2*z2
print 'y2*z2/2:\n', y2*z2/2

y_sum = y.sum()
print 'y:\n', y
print 'y_sum:\n', y_sum
#axis=0为列和，axis=1为行和
print y.sum(axis=1)

np_n = np.ones((3,2,4))
print '--------'
print np_n
print '--------'
print np_n.sum(axis=2)
