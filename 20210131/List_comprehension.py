#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:07:01 2021

@author: JasonChang
"""

# in-place construction
arr1 = [i for i in range(10)]

print(arr1)


# in-place construction
arr1 = [i for i in range(10)]

# you can use if to filter the elements
arr2 = [x for x in arr1 if x % 2 == 0]

# you can use as many conditions as you want!
arr3 = [x for x in arr1 if x >= 3 and x % 2]

# use nested for loops to make everyone dizzy XD
arr4 = [(x, y) for x in range(3) for y in range(4)]

print(arr1)
print(arr2)
print(arr3)
print(arr4)