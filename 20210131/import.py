#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:15:21 2021

@author: JasonChang
"""

import matplotlib.pyplot as plt # import matplotlib
import numpy as np              # import numpy
x = np.linspace(0, 10, 100)     # x在0到10之間取100個元素


y = np.cos(x)                   # 將產生的x元素，代入cos()產生對應y值
z = np.sin(x)                   # 將產生的x元素，代入sin()產生對應z值
plt.plot(x, y, label='Coscoscoscos')
# plt.show()
plt.plot(x, z, label='Sinsinsinsin')
plt.legend(loc = 'upper left')
plt.show()