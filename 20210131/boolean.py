#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:25:37 2021

@author: JasonChang
"""

h = 180
w = 85
grade = 80

# 身高超過175或是體重超過80
if h > 175 or w > 80:
    print('high')

# 成績高於70但是不高於90
if grade > 70 and grade < 90:
    print('good')