import numpy as np
import pandas as pd

def generate_sales_data(clients=5, days=7):
    np.random.seed(42)
    return np.random.randint(100, 500, size=(clients, days))

def calculate_statistics(sales_data):
    return {
        "Total Sales": np.sum(sales_data, axis=1),
        "Average Sales": np.mean(sales_data, axis=1),
        "Max Sales": np.max(sales_data, axis=1),
        "Min Sales": np.min(sales_data, axis=1),
        "Std Dev Sales": np.std(sales_data, axis=1)
    }

def export_summary(statistics):
    df = pd.DataFrame(statistics)
    print("\nClient Sales Summary:\n", df)
    df.to_csv("sales_summary.csv", index=False)
    print("\nSales summary saved as 'sales_summary.csv'.")

def main():
    sales_data = generate_sales_data()
    stats = calculate_statistics(sales_data)
    export_summary(stats)

if __name__ == "__main__":
    main()