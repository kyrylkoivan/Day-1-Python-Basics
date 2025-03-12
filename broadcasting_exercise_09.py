import numpy as np

# Given points
points_A = np.array([[1, 2], [3, 4], [5, 6]])
points_B = np.array([[2, 3], [4, 5], [6, 7]])

# Compute Euclidean distance
distances = np.linalg.norm(points_B - points_A, axis=1)

print("Euclidean Distances:", distances)
