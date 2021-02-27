# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:23:58 2021

@author: paul8
"""

import numpy as np

# 陣列元素可以使用 list 或 tuple 傳入
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [-1, -2, -3]])

# 注意：矩陣乘法需要 第一個欄數等於第二個矩陣列數
#result_1 = A.dot(C)
print("A:", A)
print("B:", B)
print("A+B:", A+B)
print("A-B:", A-B)
print("A*B:", A*B)
print("A/B:", A/B)

# In[]
E = np.array([1, 2, 3, -1, -2])
a = E[0]

j = 1
while j < 5:
    if E[j] > a:  # E[1]
        a = E[j]
    j+=1 # j = j + 1

print("Highest value is:", a)

#print("Higest value is:{}".format(a))
#for i in range(1,5):
#    if E[i] > a:
#        a = E[i]
#print("Higest value is:{}".format(a))

# In[]

C = np.array([1, 2, 3])
D = np.array([7, -2, 3])

for i in range(3):
    if C[i] > D[i]:
        print("C[{}] is larger than D[{}]".format(i, i))
    elif C[i] < D[i]:
        print("C[{}] is smaller than D[{}]".format(i, i))
    else:
        print("C[{}] is same as D[{}]".format(i, i))