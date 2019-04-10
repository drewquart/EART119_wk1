# -*- coding: utf-8 -*-
"""
    script that tests numpy functionality
"""

import numpy

start = 1
step = 1
stop = 10  # stopping value of vector -1
N = 10     # Number of elements in our vector

aV = numpy.arange(start, stop, step)  # Stops at n-1
print(aV)

aV2 = numpy.linspace(start, stop, N, dtype = int)  # Gives exactly 10 elements
print(aV2)
