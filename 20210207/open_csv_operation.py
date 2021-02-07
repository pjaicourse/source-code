#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:34:36 2021

@author: JasonChang
"""

import numpy as np
import matplotlib.pyplot as plt


f = open('data.csv')

for line in f.readlines():
    print(line)
    
f.close



# In[]


f = open('data.csv')

for line in f.readlines():
    line.split(',')[0]
    # print(line.split(',')[0])
f.close



# In[]

out = np.array([])
out_tmp = np.array([1])



f = open('data.csv')

for line in f.readlines():
    
    out_tmp = line.split(',')[0]
    out = np.append(out, out_tmp)
    
    
f.close

plt.plot(out)
plt.show()


    
# In[]
    
import wave, struct

out = np.array([])
out_tmp = np.array([1])


wavefile = wave.open('demo.wav', 'r')

length = wavefile.getnframes()
for i in range(0, length):
    wavedata = wavefile.readframes(1)
    data = struct.unpack("<h", wavedata)
    out_tmp[0] = int(data[0])
    out = np.append(out, out_tmp)
    

np.save('out',out)
    
plt.plot(out)
plt.show()





# In[]



f = open("song_demo.txt", "w")

for i in range(len(out)):
    f.write(str(out[i])+'\n')    



f.close()


