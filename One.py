# Kate Williams
# 6/19/2018

# Import packages

import numpy as np
import matplotlib.pyplot as mpl

# Create lists
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
mpl.plot(x, y, 'bo')
mpl.show()  # Plot initial points

# y = mx + b
# Find m (slope)
mx = np.mean(x)  # The mean of x
my = np.mean(y)  # The mean of y
i = 0  # Counter variable
num = 0  # Final slope
den = 0
while i < len(x):  # For every number in x and y
    num += (x[i] - mx) * (y[i] - my)
    den += (x[i] - mx) * (x[i] - mx)
    i += 1
m = round(num/den, 2)
# Find b (y intercept)
b = 1

print(len(y))
y2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # New empty list
j = 0  # Counter variable
#m = 0.6
while j < len(y):
    y2[j] = (m * x[j]) + b
    j += 1

mpl.plot(x, y, 'bo')
mpl.plot(x, y2)
mpl.show()
print(x, y2)
