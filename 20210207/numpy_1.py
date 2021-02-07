#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:04:16 2021

@author: JasonChang
"""

# 引入套件，使用 as 代表別名，可以讓我們少打一點字
import numpy as np


# 陣列元素可以使用 list 或 tuple 傳入
A = np.array([4, 5, 6])
B = np.array((1, 2, 3))

# 印出結果
print(A)
print(B)

# 印出型別
print(type(A))
print(type(B))


# 更改資料
A[0] = 12

B[1] = 14
B[2] = 9
# 印出更改結果
print(A)
print(B)