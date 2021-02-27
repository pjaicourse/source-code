# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:05:42 2021

@author: paul8
"""

age = input('Hello, enter your age.')

if float(age) > 18:
    print('age is ', age, ', you are adult.')
else:
    print('age is ', age, ', you are not adult.')

# In[]
    
str1 = 'My,name,is,'
str2 = 'Paul.'
# str2[0] = 'y'
# a = a + b could be written as a += b
str3 = str1 + str2
print(str3)
# print(str1 is str1)
# print(str1 == str1)
# print(str1)

result = str3.split(',')
# print(str2)
print(result)

# result_back = '***'.join(result)
# print(result_back)


