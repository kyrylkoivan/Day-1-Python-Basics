import numpy as np

# Given prices
prices = np.array([100, 200, 300, 400, 500])

# Given discount rates
discount_rates = np.array([0.10, 0.15, 0.20, 0.25, 0.30])

# Compute discounted prices
discounted_prices = prices * (1 - discount_rates)

print("Discounted Prices:", discounted_prices)
