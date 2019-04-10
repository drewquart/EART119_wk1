#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:23:47 2019

@author: andrewquartuccio
"""

import matplotlib.pyplot as plt
import numpy as np

v0 = 5
g = 9.81
t = np.linspace(0, 1, 1001)

y = v0*t - 0.5*g*t**2

plt.plot(t, y)
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()