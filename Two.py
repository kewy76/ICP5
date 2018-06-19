# Kate Williams
# 6/19/2018

import numpy as np
import math
import matplotlib.pyplot as mpl

n = input("How many points do you want: ")

# Create random arrays
heights = np.random.randint(152, 213, int(n))  # Heights in centimeters
weights = np.random.randint(52, 68, int(n))  # Weights in kilograms

mpl.plot(heights, weights, 'ro')
mpl.show()

k = np.random.randint(0, int(n) - 1, 3)  # Pick centroids
one = k[0]
two = k[1]
three = k[2]
distances = np.zeros((int(n), 3))  # Empty 2d array to store distances
i = 0  # Counter variable

while i < len(heights):  # Define the distances in between each point and the centroids
    distances[i, 0] = round(math.sqrt(((heights[i] - heights[one]) ** 2) + ((weights[i] - weights[one]) ** 2)), 2)
    distances[i, 1] = round(math.sqrt(((heights[i] - heights[two]) ** 2) + ((weights[i] - weights[two]) ** 2)), 2)
    distances[i, 2] = round(math.sqrt(((heights[i] - heights[three]) ** 2) + ((weights[i] - weights[three]) ** 2)), 2)
    i += 1

# Define clusters
cluster1 = []
cluster2 = []
cluster3 = []

j = 0  # Counter variable

while j < len(heights):  # Pick the closest centroid and assign clusters
    if np.min(distances[j]) == distances[j, 0]:
        cluster1.append(j)
    if np.min(distances[j]) == distances[j, 1]:
        cluster2.append(j)
    else:
        cluster3.append(j)
    j += 1

mpl.plot(cluster1, 'ro')
mpl.plot(cluster2, 'bo')
mpl.plot(cluster3, 'yo')
mpl.show()