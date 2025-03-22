import numpy as np
import pandas as pd

# Simulated dataset: Each row represents a customer
# Columns: [Customer ID, Purchase Amount]
customers = np.array([
    [101, 250.0],
    [102, 400.0],
    [103, 150.0],
    [104, 600.0],
    [105, 350.0],
])

# Customer categories based on Purchase Amount
# High spenders (>500) get 20% discount, mid spenders (200-500) get 10%,
# low spenders (<200) get 5%
discount_rates = np.array([0.05, 0.10, 0.20])

# Apply broadcasting to determine the discount rate for each customer
conditions = [
    customers[:, 1] < 200,  # Low spenders
    (customers[:, 1] >= 200) & (customers[:, 1] <= 500),  # Mid spenders
    customers[:, 1] > 500  # High spenders
]

# Assign appropriate discount rates
customer_discounts = np.select(conditions, discount_rates)

# Calculate final prices after applying the discount
final_prices = customers[:, 1] * (1 - customer_discounts)

# Combine results into a structured NumPy array
final_data = np.column_stack((customers, customer_discounts, final_prices))

# Convert to Pandas DataFrame for better readability
columns = ["Customer ID", "Purchase Amount", "Discount Rate", "Final Price"]
df = pd.DataFrame(final_data, columns=columns)

# Display the final results
df["Customer ID"] = df["Customer ID"].astype(int)
# Convert Customer ID to integer for clarity
print(df)

# Save results to CSV
df.to_csv("discounted_customers.csv", index=False)
