# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 11, 1)
plt.plot(x, x*2)
plt.plot(x, x*3)
plt.plot(x, x*4)
plt.legend(['Normal', 'Fast', 'Faster'])
plt.show()