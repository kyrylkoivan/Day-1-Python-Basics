import numpy as np

# Given dataset with NaN values
data = np.array([
    [10, np.nan, 30, 40],
    [20, 50, np.nan, 70],
    [np.nan, 20, 40, 80],
    [25, 35, 45, np.nan],
    [np.nan, 60, 70, 90]
])

# Compute column-wise means, ignoring NaN values
col_means = np.nanmean(data, axis=0)

# Replace NaN values with column means
filled_data = np.where(np.isnan(data), col_means, data)

print("Data After Filling NaNs:\n", filled_data)
