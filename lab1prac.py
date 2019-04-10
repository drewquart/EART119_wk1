#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:02:41 2019
   Practice summation 1-100 
@author: andrewquartuccio
"""

n = 100  # Ending value of summation
sum = 0    

for i in range(1,n+1,1):
    sum += i
    
print(sum)