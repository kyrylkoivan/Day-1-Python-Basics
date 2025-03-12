import numpy as np

# Given sales data (3 stores, 4 products)
sales = np.array([
    [1200, 1500, 1600, 1800],
    [2200, 2500, 2600, 2800],
    [3200, 3500, 3600, 3800]
])

# Given tax rates per store
tax_rates = np.array([[0.05], [0.07], [0.10]])  # Reshaped to column vector

# Apply tax and calculate final prices
final_prices = sales * (1 + tax_rates)

print("Sales After Tax:\n", final_prices)
