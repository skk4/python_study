# -*- coding:utf-8 -*-
'''
解题思路
move(塔层数, 起点, 缓冲区, 终点）
第一步:先把'塔层数-1', 从'起点'->'缓冲区', 当调用move()函数时, 这个缓冲区就是我们要的终点,
             函数为move(塔层数-1, 起点, 终点, 缓冲区)

第二步:然后把最后一个塔, 从'起点'->'终点',函数为move(1, 起点, 缓冲区, 终点)
第三步:最后把 '缓冲区'上'塔层数-1'移动到终点,当调用函数时,'缓冲区'作为起点,'终点'还是'终点','起点'变为缓冲区
     函数为move(塔层数-1,缓冲区, 起点, 终点)
'''

def move(n, x, y, z):
    if n == 1:
        print x,'->',z
    else:
        move(n-1, x, z, y)
        move(1, x, y, z)
        move(n-1, y, x, z)
        
move(20, 'x', 'y', 'z')        