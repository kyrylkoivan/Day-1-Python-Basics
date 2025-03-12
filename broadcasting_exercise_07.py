import numpy as np

# Given yearly spending data
spending = np.array([500, 1200, 3200, 4500, 8000, 10000])

# Define conditions
conditions = [spending < 1000, (spending >= 1000) & (spending <= 5000), spending > 5000]
choices = ['Low', 'Mid', 'High']

# Apply np.select with explicit dtype to prevent type errors
segments = np.select(conditions, choices, default='Unknown').astype(object)

print("Customer Segments:", segments)
