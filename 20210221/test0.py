# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:43:03 2021

@author: paul8
"""

# In[]
f = open("test_0.txt", "w")
f.write("0.2 0.9 0.8\n1.0 0.1 0.2\n0.5 0.7 0.8")

f.close()


# In[]
f = open("test_0.txt", "r")

for line in f.readlines():
    #print(line.split(' ')[0])
    x0 = line.split(',')[0]
    x1 = line.split(' ')[1]
    x2 = line.split(' ')[2]
    
    print(x1)
    
f.close
