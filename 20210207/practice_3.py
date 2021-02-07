#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:47:53 2021

@author: JasonChang
"""

# Method 1

arr1 = []
arr2 = []

for i in range(20):
    if i % 2 == 1:
        arr1.append(i)
    if i % 2 == 0:
        arr2.append(i)
print(arr1)
print(arr2)

for index in range(len(arr1)):
    print(arr1[index], '<--->', arr2[index])

# Method 2

arr1 = [i for i in range(1, 21) if i % 2 == 1]
arr2 = [i for i in range(1, 21) if i % 2 == 0]


for index in range(len(arr1)):
    print(arr1[index], '<--->', arr2[index])