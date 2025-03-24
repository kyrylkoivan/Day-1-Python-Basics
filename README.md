# 🚀 Client Sales Data Automation & Analysis

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Setup & Environment Configuration](#setup--environment-configuration)
- [Implemented Features](#implemented-features)
- [Detailed Workflow Summary](#detailed-workflow-summary)
- [Key Learnings](#key-learnings)
- [Next Steps](#next-steps)
- [How to Run](#how-to-run)
- [Contributing](#contributing)

---

## 🚀 Project Overview

This repository showcases a comprehensive, production-ready workflow designed to automate, validate, and analyze client sales data using **Python, NumPy, Pandas, Great Expectations, and Git**.

It includes:

1. **NumPy-powered statistical sales analysis.**
2. **Dynamic discount calculations using broadcasting.**
3. **ETL scripts for dataset merging and cleaning.**
4. **Advanced exception handling.**
5. **File automation scripts (renaming, sorting).**
6. **Great Expectations integration for robust data validation.**
7. **Systematic version control with feature branches, rebasing, and clean commit histories.**
8. **Professional documentation, PEP-8 compliance, and polished LinkedIn updates.**

---

## 📂 Repository Structure

```
├── README.md
├── requirements.txt
├── venv/                      # Virtual environment (excluded from Git)
├── data/                      # Contains all datasets and CSV files
│   └── sales_dataset_1.csv
│   └── sales_dataset_2.csv
│   └── sales_dataset_3.csv
│   └── merged_sales_data.csv
├── scripts/                   # All Python scripts neatly organized
│   └── client_inventory.py
│   └── numpy_discount_calc.py
│   └── sales_analysis.py
│   └── data_merge.py
│   └── file_automation.py
│   └── list_dict_practice.py
│   └── exception_practice.py
│   └── broadcasting_exercise_01.py - broadcasting_exercise_10.py
│   └── user_info_formatter.py
├── great_expectations/        # Great Expectations project directory
├── day1_plan.md               # Task scope & plan documentation
└── .gitignore                 # Excludes venv/, __pycache__/, datasets, exports
```

---

## ⚙️ Setup & Environment Configuration

This environment was built for **scalability, maintainability, and production-level standards**. Here's how to replicate and configure it:

### 📦 Dependencies

- **Python 3.10+**
- `numpy`
- `pandas`
- `great_expectations`
- `python-dotenv` (optional)
- `pytest` (optional)

### 🖥 Installation Instructions

```bash
# 1️⃣ Clone the repository
git clone <your-repo-link>
cd <repo-name>

# 2️⃣ Set up a virtual environment
python -m venv venv
# Activate virtual environment:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3️⃣ Upgrade pip & install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# If requirements.txt not available:
pip install numpy pandas great_expectations python-dotenv pytest
```

---

## ✨ Implemented Features

✅ **Professional Repo Structure**  
Scripts, datasets, configs clearly separated.

✅ **Feature Branch Workflow**  
All new functionality developed in dedicated branches, tested, cleanly merged.

✅ **NumPy Automation Scripts**  
Efficient sales analysis, statistical operations, discount calculations — **no loops**, full broadcasting.

✅ **ETL Data Merging**  
Sales CSVs consolidated using Pandas, validated via Great Expectations.

✅ **Advanced Exception Handling**  
Deliberate edge cases tested, with robust try-except blocks across critical scripts.

✅ **File Automation**  
Scripts for renaming, categorizing, and sorting files via `os` and `shutil`.

✅ **PEP-8 Compliance & Modularity**  
All code follows clean standards, modular functions, clear docstrings.

✅ **Great Expectations Integration**  
Expectation suites programmatically defined, validating merged datasets before export.

✅ **Public Branding**  
Regular, polished LinkedIn updates, clean visuals, clear progress logs.

---

## 📋 Detailed Workflow Summary

### **📅 Day 1-2: Foundation Setup**
- Downloaded latest Python version, verified installation.
- Installed and configured **VS Code**.
- Completed **Codecademy** foundational exercises: print statements, variables, arithmetic, f-strings, loops, control flow.
- Scripts organized into descriptive files: `lesson1_print_statements.py`, `lesson2_variables.py`.
- Began structured note-taking (variables, conditionals, data types).
- Completed **Exercism** exercises focusing on arithmetic, type conversions, and `raise` statement error handling.
- Created, debugged, and uploaded `client_inventory.py`, using loops, control flow, and PEP-8 standards to GitHub.

### **📅 Day 3-4: NumPy Mastery**
- Set up dedicated branch: `day-3-numpy-intro`.
- Completed 15+ NumPy exercises covering:
  - Array creation, reshaping, advanced indexing.
  - Broadcasting, vectorized calculations, masking.
- Built `sales_analysis.py`: automated client sales summary (total, average, std, min/max) → output to Pandas DataFrame and CSV.
- Developed `numpy_discount_calc.py`: dynamic discount application without loops.
- Rigorous Git feature branching, commits, and clean merges.

### **📅 Day 5: Broadcasting & Exception Handling**
- Completed 10 advanced Kaggle broadcasting exercises.
- Embedded robust `try-except` blocks in `numpy_discount_calc.py` and related scripts.
- Created intentional Git conflicts, resolved and documented them.
- Finalized feature branch, merged, shared progress on LinkedIn with visuals.

### **📅 Day 6: File Automation Focus**
- Objective set in `Notion`.
- Built `file_automation.py` using `os` and `shutil`:
  - File renaming.
  - Categorizing by extensions (.pdf, .csv, .jpg).
  - Exception handling for missing files, permission issues.
- Extensive dummy file testing.
- Documented, committed, merged into main.
- LinkedIn post shared with clear visuals, encouraging feedback.

### **📅 Day 7: Refactoring & Git Mastery**
- Refactored all major scripts:
  - Modular functions.
  - Clean docstrings.
  - PEP-8 compliance.
- Mastered **Git rebasing, squashing**, cleaned commit histories.
- Enhanced README files with clear setup instructions.
- Polished LinkedIn post with Canva visual showcasing automation work.

### **📅 Week 2, Day 1: Data Merging & Validation**
- Reorganized GitHub repo:
  - `/scripts` → All scripts.
  - `/data` → All datasets.
- Created `feature/data-merge` branch.
- Developed `data_merge.py` merging three sales CSVs.
- Set up **virtual environment**, installed:
  - Pandas, Great Expectations.
- Initialized **Great Expectations project**, programmatically defined expectation suites.
- Verified merged dataset quality, exported to `sales_consolidated.csv`.
- Documented everything in `README.md`, clear commit history maintained.

---

## 📚 Key Learnings

1. **NumPy Broadcasting & Vectorized Computation**:  
Efficient large-scale data manipulation without loops.

2. **Professional Git Workflow**:  
Branching, merging, rebasing, squashing — all used to maintain clean histories.

3. **Data Validation Discipline**:  
Applied Great Expectations to enforce data quality checks programmatically.

4. **Exception Handling Best Practices**:  
Integrated and tested exception handling under various scenarios.

5. **File Automation & Real-World ETL**:  
Built scalable scripts automating file operations, dataset merges, and exports.

6. **PEP-8 Compliance & Documentation**:  
Maintained high code standards, docstrings, modular functions, clear comments.

7. **Public Portfolio Development**:  
Shared polished, methodical progress updates on LinkedIn, building strong branding.

---

## 🚀 Next Steps

- Integrate **Matplotlib/Seaborn** for sales trend visualizations.
- Expand ETL pipelines to pull real-world APIs/datasets.
- Add **pytest** unit tests across key scripts.
- Experiment with **NumPy-based machine learning models**.
- Package scripts into a deployable solution (CLI or web interface).

---

## 🛠 How to Run

```bash
# Clone repo
git clone <your-repo-link>
cd <repo-name>

# Set up virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run key scripts:
python scripts/sales_analysis.py
python scripts/numpy_discount_calc.py
python scripts/data_merge.py
python scripts/file_automation.py

# Run Great Expectations data validation
great_expectations checkpoint run sales_data_checkpoint
```

---

## 🤝 Contributing

Contributions, suggestions, and constructive feedback are welcome.  
Feel free to fork, submit pull requests, or reach out via [LinkedIn](www.linkedin.com/in/ivan-k-573b74330).

---
```
