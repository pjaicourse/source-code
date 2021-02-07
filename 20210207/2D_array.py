#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:09:55 2021

@author: JasonChang
"""

import numpy as np

# 陣列元素可以使用 list 或 tuple 傳入
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])

result_1 = A + B

print(result_1)


# 陣列元素可以使用 list 或 tuple 傳入
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])

result_1 = A - B

print(result_1)




A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])

# 亦可使用 np.multiply(A, B)
result_1 = A * B

print(result_1)




A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])

result_1 = A / B

print(result_1)



A = np.array([[1, 2, 3], [4, 5, 6]])

print(A.T)