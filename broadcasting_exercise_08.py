import numpy as np

# Given purchases and discount rates
purchases = np.array([
    [200, 300, 400],
    [500, 600, 700],
    [800, 900, 1000],
    [1100, 1200, 1300],
    [1400, 1500, 1600]
])
discount_rates = np.array([[0.05], [0.10], [0.15], [0.20], [0.25]])

# Apply discounts
discounted_purchases = purchases * (1 - discount_rates)

print("Discounted Purchases:\n", discounted_purchases)
