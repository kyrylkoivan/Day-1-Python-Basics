import numpy as np
import pandas as pd

# Generate mock sales data: 5 clients, 7 days of sales
np.random.seed(42)  # Set seed for reproducibility
sales_data = np.random.randint(100, 500, size=(5, 7))

# Calculate key statistics for each client
total_sales = np.sum(sales_data, axis=1)  # Sum of all sales per client
average_sales = np.mean(sales_data, axis=1)  # Average daily sales per client
max_sales = np.max(sales_data, axis=1)  # Maximum sales per client
min_sales = np.min(sales_data, axis=1)  # Minimum sales per client
std_dev_sales = np.std(sales_data, axis=1)  # Standard deviation of sales

# Create a DataFrame for better visualization
sales_summary = pd.DataFrame({
    "Total Sales": total_sales,
    "Average Sales": average_sales,
    "Max Sales": max_sales,
    "Min Sales": min_sales,
    "Std Dev Sales": std_dev_sales
})

# Display sales summary
print("Client Sales Summary:\n", sales_summary)

# Save the processed data to a CSV file
sales_summary.to_csv("sales_summary.csv", index=False)
print("\nSales summary saved as 'sales_summary.csv'.")
