# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 100)
fig1 = plt.figure()
ax1 = fig1.add_subplot(2,2,1)
ax2 = fig1.add_subplot(2,2,2)
ax1.plot(x, x)
ax1.set_xlim(0, 50)
ax1.set_xticklabels(['a', 'b', 'c', 'd', 'e', 'f'])

ax2.plot(x, x)
plt.show()