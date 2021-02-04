#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:02:35 2021

@author: JasonChang
"""

iv = 10 ##整數型態
fv = 12.3 ##浮點數型態
cv = 3 + 5j  ##複數型態
sv = 'hello python' ##字串型態
bv = True  ## 布林型態
nv = None  ## 空型態


print(iv, fv, cv, sv, bv)
print(type(iv))
print(type(fv))
print(type(cv))
print(type(sv))
print(type(bv))
print(nv)
print(isinstance(sv, str))