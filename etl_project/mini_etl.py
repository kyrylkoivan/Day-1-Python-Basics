"""
Mini ETL Script
---------------
This script performs a simple ETL (Extract, Transform, Load) process:
- Extract: Reads data from a CSV file.
- Transform: Cleans, filters, and aggregates key insights.
- Load: Saves the processed data into a new CSV file.

Author: Ivan Kyrylko
"""

import csv
import os

def extract_data(input_file):
    """Reads data from a CSV file and returns a list of dictionaries."""
    data = []
    try:
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    return data


def transform_data(data):
    """Cleans, filters, and processes the data for analysis."""
    processed_data = []
    
    for row in data:
        try:
            # Convert numeric values from strings to integers
            row['Age'] = int(row['Age']) if row['Age'].isdigit() else None
            row['Salary'] = float(row['Salary']) if row['Salary'].replace('.', '', 1).isdigit() else None
            
            # Filter out records with missing values
            if row['Age'] is not None and row['Salary'] is not None:
                processed_data.append(row)
        except KeyError:
            print("Error: Missing expected columns in the data.")
    
    return processed_data


def load_data(output_file, data):
    """Saves the transformed data into a new CSV file."""
    if not data:
        print("No data to save.")
        return
    
    fieldnames = data[0].keys()
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Processed data saved to {output_file}")


def main():
    """Executes the ETL process."""
    input_file = "raw_data.csv"  # Input CSV file
    output_file = "processed_data.csv"  # Output CSV file
    
    print("Starting ETL process...")
    
    # Extract step
    print("Extracting data...")
    data = extract_data(input_file)
    
    # Transform step
    print("Transforming data...")
    transformed_data = transform_data(data)
    
    # Load step
    print("Loading data...")
    load_data(output_file, transformed_data)
    
    print("ETL process completed successfully!")


if __name__ == "__main__":
    main()
