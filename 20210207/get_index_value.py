#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:06:15 2021

@author: JasonChang
"""

# 引入套件，使用 as 代表別名，可以讓我們少打一點字
import numpy as np

# 陣列元素可以使用 list 或 tuple 傳入
array_1 = np.array([1, 2, 3])

print(array_1[0])
array_1[0] = 7


# 取 1 到 3（不含）元素
print(array_1[0:3])



######################################
# 透過 mask 布林遮罩可以決定要取出哪些符合條件的元素陣列
# 符合的只有 index 2，元素為 3 的值
# mask = (array_1 % 3 == 0)
# print(array_1[mask])