import numpy as np
import pandas as pd

try:
    # Simulated dataset
    customers = np.array([
        [101, 250.0],
        [102, 400.0],
        [103, 150.0],
        [104, 600.0],
        [105, 350.0],
    ])

    # Discount categories
    discount_rates = np.array([0.05, 0.10, 0.20])

    # **Step 1: Ensure correct shape of customers array**
    if customers.shape[1] != 2:
        raise ValueError(
            "Shape Mismatch: Customer data must have exactly 2 columns (ID and Purchase Amount). "
            "Check if the dataset was loaded correctly."
        )

    # **Step 2: Define Conditions for Discount Categories**
    try:
        conditions = [
            customers[:, 1] < 200,
            (customers[:, 1] >= 200) & (customers[:, 1] <= 500),
            customers[:, 1] > 500
        ]
    except IndexError as ie:
        raise IndexError(
            "Indexing Error: Ensure the second column contains valid purchase amounts. "
            "Verify that the dataset has no missing or malformed rows."
        ) from ie

    # **Step 3: Apply Discounts Using NumPy Broadcasting**
    try:
        customer_discounts = np.select(conditions, discount_rates, default=0)
    except ValueError as ve:
        raise ValueError(
            "NumPy Broadcasting Error: Failed to apply discount rates. "
            "Check if conditions and discount_rates match in length."
        ) from ve

    # **Step 4: Calculate Final Prices**
    try:
        final_prices = customers[:, 1] * (1 - customer_discounts)
    except TypeError as te:
        raise TypeError(
            "Multiplication Error: Ensure purchase amounts and discount rates are numeric. "
            "Check for unexpected data types in the dataset."
        ) from te

    # **Step 5: Combine Data into a Single Array**
    try:
        final_data = np.column_stack((customers, customer_discounts, final_prices))
    except ValueError as ve:
        raise ValueError(
            "Array Stacking Error: Ensure all arrays have matching dimensions. "
            "Check for inconsistent row counts in different arrays."
        ) from ve

    # **Step 6: Convert to Pandas DataFrame**
    try:
        columns = ["Customer ID", "Purchase Amount", "Discount Rate", "Final Price"]
        df = pd.DataFrame(final_data, columns=columns)
        df["Customer ID"] = df["Customer ID"].astype(int)  # Convert Customer ID to integer
    except TypeError as te:
        raise TypeError(
            "Data Conversion Error: Failed to convert Customer ID to an integer. "
            "Verify that all values are properly formatted."
        ) from te

    # **Step 7: Display and Save Results**
    try:
        print(df)  # Display DataFrame
        df.to_csv("discounted_customers.csv", index=False)  # Save to CSV
    except Exception as e:
        raise Exception(
            "Unexpected File Handling Error: Failed to save or display the DataFrame. "
            "Check file permissions and available disk space."
        ) from e

# **Step 8: Catch General Errors**
except ValueError as ve:
    print(f"ValueError: {ve}")

except TypeError as te:
    print(f"TypeError: {te}")

except IndexError as ie:
    print(f"IndexError: {ie}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
