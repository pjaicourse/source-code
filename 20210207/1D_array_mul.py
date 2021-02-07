#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:08:24 2021

@author: JasonChang
"""

import numpy as np

# 陣列元素可以使用 list 或 tuple 傳入
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

result_1 = A + B
print(result_1)
result_1 = A - B
print(result_1)
result_1 = A * B
print(result_1)
result_1 = A / B
print(result_1)