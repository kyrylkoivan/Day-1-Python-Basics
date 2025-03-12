import numpy as np

# Given scores and weights
scores = np.array([
    [85, 90, 95],
    [78, 82, 88],
    [92, 94, 96]
])
weights = np.array([0.2, 0.3, 0.5])

# Compute weighted averages
weighted_averages = np.sum(scores * weights, axis=1)

print("Weighted Averages:", weighted_averages)
