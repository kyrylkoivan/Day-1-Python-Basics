import numpy as np
import pandas as pd

def validate_customers(customers):
    if customers.shape[1] != 2:
        raise ValueError("Customers data must have 2 columns (ID, Amount).")

def calculate_discounts(customers):
    conditions = [
        customers[:, 1] < 200,
        (customers[:, 1] >= 200) & (customers[:, 1] <= 500),
        customers[:, 1] > 500
    ]
    rates = np.array([0.05, 0.10, 0.20])
    return np.select(conditions, rates, default=0)

def compute_final_prices(customers, discounts):
    return customers[:, 1] * (1 - discounts)

def create_discount_df(customers, discounts, final_prices):
    df = pd.DataFrame(
        np.column_stack((customers, discounts, final_prices)),
        columns=["Customer ID", "Purchase Amount", "Discount Rate", "Final Price"]
    )
    df["Customer ID"] = df["Customer ID"].astype(int)
    return df

def process_discounts():
    try:
        customers = np.array([
            [101, 250.0],
            [102, 400.0],
            [103, 150.0],
            [104, 600.0],
            [105, 350.0],
        ])

        validate_customers(customers)
        discounts = calculate_discounts(customers)
        final_prices = compute_final_prices(customers, discounts)
        df = create_discount_df(customers, discounts, final_prices)
        print(df)
        df.to_csv("discounted_customers.csv", index=False)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    process_discounts()
