#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:42:15 2019
    Wk 1 Problem Set
@author: andrewquartuccio
"""

import numpy as np

#   Practice Summation

n = 10
x = 0

for i in range(1,n+1):
    x += 5*i

print("Summation of Problem #1: " + str(x)+'\n')


#    Approximation of Pi


approx_pi = 0

for i in range(n+1):
    approx_pi += 8./((4.*i + 1.)*(4.*i + 3.))


print("Approximation of Pi w/ 10 iterations: " +str(approx_pi))
err = np.pi - approx_pi
print("Error of Pi Approximation: " +str(err)+'\n')

n  = 50
approx_pi = 0

for i in range(n+1):
    approx_pi += 8./((4.*i + 1.)*(4.*i + 3.))


print("Approximation of Pi w/ 50 iterations: " +str(approx_pi))
err = np.pi - approx_pi
print("Error of Pi Approximation: " +str(err)+'\n')

n = 100
approx_pi = 0

for i in range(n+1):
    approx_pi += 8./((4.*i + 1.)*(4.*i + 3.))


print("Approximation of Pi w/ 100 iterations: " +str(approx_pi))
err = np.pi - approx_pi
print("Error of Pi Approximation: " +str(err)+'\n')

n=1000
approx_pi = 0

for i in range(n+1):
    approx_pi += 8./((4.*i + 1.)*(4.*i + 3.))


print("Approximation of Pi w/ 1000 iterations: " +str(approx_pi))
err = np.pi - approx_pi
print("Error of Pi Approximation: " +str(err)+'\n')