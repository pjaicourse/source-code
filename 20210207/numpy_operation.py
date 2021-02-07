#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:11:29 2021

@author: JasonChang
"""

# dot product

import numpy as np

# 陣列元素可以使用 list 或 tuple 傳入
A = np.array([[1, 2, 3], [4, 5, 6]])
C = np.array([[7, 8, 9], [1, 2, 3], [1, 2, 3]])

# 注意：矩陣乘法需要 第一個欄數等於第二個矩陣列數
result_1 = A.dot(C)

print(result_1)


# In[]


# inner production

import numpy as np

# 陣列元素可以使用 list 或 tuple 傳入
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])

result_1 = np.inner(A, B)

print(result_1)


# In[]


# outer production



import numpy as np

# 陣列元素可以使用 list 或 tuple 傳入
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])

result_1 = np.outer(A, B)

print(result_1)








