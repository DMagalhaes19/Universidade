# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:11:56 2020

@author: alexd
"""
result=0
for i in range(1,5+1):
    result += i**2
print(result)

for i in range(1,5+1):
    for j in range(5,0+1):
        print((i+j) % 2)
        

for i in range(20):
    if(i==5 or i==10):
        continue
    else:
        print(i,end =' ')    
        