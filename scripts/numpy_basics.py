# ===========================
# NumPy Basics: Creating & Slicing Arrays
# ===========================
import numpy as np

# --------------------------
# Exercise 1: Create a 1D NumPy array from a Python list
# --------------------------
array_1d = np.array([10, 20, 30, 40, 50])
print("Exercise 1 - 1D NumPy Array:", array_1d)

# --------------------------
# Exercise 2: Create a 2D NumPy array (matrix)
# --------------------------
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Exercise 2 - 2D NumPy Array:\n", array_2d)

# --------------------------
# Exercise 3: Create an array of zeros with shape (3, 4)
# --------------------------
zeros_array = np.zeros((3, 4))
print("Exercise 3 - Array of Zeros:\n", zeros_array)

# --------------------------
# Exercise 4: Create an array of ones with shape (2, 5)
# --------------------------
ones_array = np.ones((2, 5))
print("Exercise 4 - Array of Ones:\n", ones_array)

# --------------------------
# Exercise 5: Create an array of evenly spaced values from 0 to 20 (step=5)
# --------------------------
evenly_spaced = np.arange(0, 21, 5)
print("Exercise 5 - Evenly Spaced Array:", evenly_spaced)

# --------------------------
# Exercise 6: Slice a 1D array (extract elements 2, 3, and 4)
# --------------------------
sliced_1d = array_1d[1:4]
print("Exercise 6 - Sliced 1D Array:", sliced_1d)

# --------------------------
# Exercise 7: Slice a 2D array (extract a sub-matrix)
# --------------------------
sliced_2d = array_2d[0:2, 1:3]  # Extract rows 0-1, columns 1-2
print("Exercise 7 - Sliced 2D Array:\n", sliced_2d)

# --------------------------
# Exercise 8: Reshape a 1D array into a 2D array
# --------------------------
reshaped_array = np.arange(1, 10).reshape(3, 3)
print("Exercise 8 - Reshaped 1D Array into 3x3 Matrix:\n", reshaped_array)

# --------------------------
# Exercise 9: Get specific elements from a 2D array
# --------------------------
element = array_2d[2, 1]  # Extract element at row index 2, column index 1
print("Exercise 9 - Specific Element from 2D Array:", element)

# --------------------------
# Exercise 10: Reverse a NumPy array
# --------------------------
reversed_array = array_1d[::-1]
print("Exercise 10 - Reversed 1D Array:", reversed_array)
