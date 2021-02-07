#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:22:08 2021

@author: JasonChang
"""


#open and read the file after the appending:
f = open("demo_file_1.txt", "r")
print(f.read())


f = open("demo_file_1.txt", "a")
f.write("Now the file has more content!\n")
f.close()



# In[]


f = open("demo_csv_1.csv", "r")
print(f.read())