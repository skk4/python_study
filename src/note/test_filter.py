# -*- coding:utf-8 -*-
numblist= [1, True, 3, False, 0, 9]
print filter(None, numblist)
#过滤掉返回值为False的数据

numblist2 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
def odd(x):
    return not x%2
    
print filter(odd, numblist2)
#过滤掉返回值为False的数据,结果为：[2, 4, 6, 8]


f = lambda x: not x%2
print filter(f, numblist2)