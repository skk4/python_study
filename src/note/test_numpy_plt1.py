# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
'''
#颜色
b:blue 
g:green
r:red
c:cyan
m:magenta
y:yellow
k:black
w:white
#线性
- 实线
--虚线
-.点划线 
：点线
'''
'''
#点状
"."point
","pixel
"o"circle
"v"triangle_down
"^"triangle_up
"<"triangle_left
">"triangle_right
"1"tri_down
"2"tri_up
"3"tri_left
"4"tri_right
"8"octagon
"s"square
"p"pentagon
"*"star
"h"hexagon1
"H"hexagon2 
"+"plus
"x"x
"D"diamond
"d"thin_diamond
'''
x = np.arange(1, 100)
y = np.log(x)
print y
plt.subplot(221)#2行2列第1个图
plt.plot(x, x, linestyle= '--', color='magenta')
plt.subplot(222)
plt.plot(x, -x)
plt.subplot(223)
plt.plot(x, x**2)
plt.subplot(224)
plt.plot(x, np.log(x))
plt.show()
