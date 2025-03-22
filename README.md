# 🚀 NumPy Mini-Projects: Client Sales Analysis & Discount Calculation

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Client Sales Data Analysis](#client-sales-data-analysis)
- [NumPy Discount Calculation Script](#numpy-discount-calculation-script)
- [What I Learned](#what-i-learned)
- [Next Steps](#next-steps)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Contributing](#contributing)

---

## 📌 Project Overview
This repository contains **two NumPy-powered mini-projects** that demonstrate efficient data processing, broadcasting, and statistical analysis:

1. **Client Sales Data Analysis** - Automates statistical calculations on mock client sales data.
2. **NumPy Discount Calculation** - Applies dynamic discount rates to a fictional customer dataset using **NumPy broadcasting**.

These projects utilize **NumPy, Pandas, and Python** to efficiently manipulate data and automate numerical analysis tasks.

---

## 📂 Repository Structure

| File/Folder               | Description                                                       |
|--------------------------|-------------------------------------------------------------------|
| `client_inventory.py`     | Manages client inventories using nested dictionaries.             |
| `client_discount.py`      | Applies dynamic discounts based on customer data.                 |
| `sales_analysis.py`       | Automates statistical analysis on client sales using NumPy.       |
| `numpy_discount_calc.py`  | Demonstrates broadcasting for efficient discount application.     |
| `exception_practice.py`   | Practice scripts for handling common Python exceptions.           |
| `user_info_formatter.py`  | Formats structured user data with advanced string methods.        |
| `sales_summary.csv`       | Output CSV of client sales summary.                               |
| `discounted_customers.csv`| Output CSV of discounted client sales data.                       |
| `README.md`               | Project documentation.                                            |

---

## 🛒 Client Sales Data Analysis
This mini-project automates the calculation and statistical analysis of mock client sales data using **NumPy**. It processes daily sales records for multiple clients, computing essential metrics like **total sales, average sales, standard deviation, minimum and maximum values**. The final structured summary is displayed in a **Pandas DataFrame** and saved as a CSV file.

### ✨ Key Features
✅ Generates mock **2D NumPy arrays** representing client sales data over a week.  
✅ Performs statistical operations, including:
   - **Total sales per client**
   - **Average daily sales**
   - **Standard deviation of sales**
   - **Maximum and minimum sales recorded**  
✅ Normalizes sales data for easier comparison.  
✅ Saves the processed results into a structured CSV file (`sales_summary.csv`).  

### 📊 Sample Output

| Client ID | Total Sales | Average Sales | Std Dev | Max Sale | Min Sale |
|----------|-------------|--------------|--------|--------|--------|
| 1001     |   $5,230    |   $747       |  $98   | $920   | $590   |
| 1002     |   $4,890    |   $698       |  $102  | $870   | $530   |

---

## 💰 NumPy Discount Calculation Script
This script simulates a **customer discount calculation system** using NumPy **broadcasting** to apply different discount rates based on purchase amounts.

### 🔹 How It Works
- Categorizes customers into **low, mid, and high spenders**.
- Applies **appropriate discount rates** using NumPy broadcasting.
- Computes final prices **without using loops**.
- Saves the structured results into a **Pandas DataFrame** and exports them to `discounted_customers.csv`.

### 🔥 Why This Matters
Using NumPy broadcasting for element-wise operations **removes the need for loops**, making the calculations much more efficient compared to traditional approaches.

---

## 📚 What I Learned
1. **NumPy is powerful for numerical analysis** – it significantly speeds up array operations compared to Python lists.  
2. **Vectorized calculations and broadcasting** help perform arithmetic operations efficiently across arrays of different shapes.  
3. **Combining NumPy with Pandas** makes it easy to structure, analyze, and export data for real-world applications.  
4. **NumPy broadcasting simplifies element-wise operations** without explicit iteration, optimizing performance.  
5. **Git Branching & Merging** – I practiced creating feature branches, resolving merge conflicts, and structuring commits properly.

---

## 🚀 Next Steps
🔹 Apply similar analysis to **real-world datasets**.  
🔹 Explore **Matplotlib and Seaborn** to visualize sales trends.  
🔹 Implement an **automated reporting system** that generates weekly insights.  
🔹 Experiment with **machine learning** by using NumPy-powered regression models.  

---

## 🛠 Setup Instructions
Ensure you have the following installed:
- Python 3.9+
- NumPy
- Pandas

Install dependencies:
```bash
pip install numpy pandas
