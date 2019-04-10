"""
    Create a list and appeend squared numbers to list
"""

lSquares = []
# loop over the natural numbers
# square, then add to list
for x in range(1,10,1):
    lSquares.append(x**2)
print(lSquares)