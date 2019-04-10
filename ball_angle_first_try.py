#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:15:39 2019

@author: andrewquartuccio
"""
from math import atan, pi


x = 10  # Horizontal Position
y = 10  # Vertical Position

angle = atan(y/x)   # Calculate angle of elevation

print(angle/pi)*180 # Display the angle in degrees

