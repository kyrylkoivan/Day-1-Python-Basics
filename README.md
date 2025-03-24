---

## 🏗️ Setup & Dependencies

This repository was carefully structured for **scalability, maintainability, and professionalism**. Below is the detailed setup guide, including environment setup, dependencies, and verification.

### 📦 Dependencies

The project leverages the following core Python libraries:

- **NumPy** – For efficient array and numerical computations.
- **Pandas** – For structured data manipulation and CSV exporting.
- **Great Expectations** – For robust data validation and quality checks.
- **Python-Dotenv** (optional) – For managing environment variables.
- **Pytest** (optional) – For future automated testing implementations.

---

### 🔥 What I Implemented

This repository is more than just scripts; it's a structured, production-ready project showcasing:

✅ **Professional Repository Structure**:  
- All scripts are cleanly organized under `/scripts`, datasets under `/data`, and configurations clearly separated.
  
✅ **Feature Branch Workflow**:  
- Each feature (e.g., data merge, file automation) was developed in a dedicated GitHub feature branch, merged cleanly after successful testing.

✅ **Version Control Mastery**:  
- Practiced branching, rebasing, squashing commits, and resolving merge conflicts.
  
✅ **Exception Handling**:  
- Integrated robust `try-except` blocks across scripts like `numpy_discount_calc.py` to handle edge cases gracefully.

✅ **PEP-8 Compliance & Modularity**:  
- All code follows Python’s PEP-8 guidelines with clean, reusable functions and detailed docstrings.

✅ **ETL Automation Scripts**:  
- Created scripts like `sales_analysis.py` and `file_automation.py` handling real-world automation tasks, file categorization, renaming, and data processing.

✅ **Data Quality Assurance**:  
- Set up **Great Expectations**, initialized a new project, and built expectation suites to ensure merged datasets' integrity.

✅ **Public Documentation & Branding**:  
- Regularly shared progress through LinkedIn posts with clean visuals, reinforcing transparency and professionalism.

---

### 🖥 Installation Instructions

To replicate the environment:

```bash
# 1️⃣ Clone the repository
git clone <your-repo-link>
cd <repo-name>

# 2️⃣ Set up a virtual environment (recommended)
python -m venv venv
# Activate virtual environment:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 3️⃣ Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# In case requirements.txt is not present, manually install:
pip install numpy pandas great_expectations python-dotenv pytest
```

---

### ✅ Verification & Testing Approach

You can verify correct installation and functionality as follows:

```bash
# Check Python version
python --version

# Check installed packages
pip list

# Run primary scripts
python scripts/sales_analysis.py
python scripts/numpy_discount_calc.py
python scripts/data_merge.py
python scripts/file_automation.py

# Validate merged datasets using Great Expectations
great_expectations checkpoint run sales_data_checkpoint
```

---

### 📂 Project Structure Overview

```
├── README.md
├── requirements.txt
├── venv/                      # Virtual environment (excluded from Git)
├── data/                      # Contains sales CSV files, datasets
│   └── sales_dataset_1.csv
│   └── sales_dataset_2.csv
│   └── sales_dataset_3.csv
├── scripts/                   # All project scripts neatly organized
│   └── client_inventory.py
│   └── numpy_discount_calc.py
│   └── sales_analysis.py
│   └── data_merge.py
│   └── list_dict_practice.py
│   └── broadcasting_exercise_01.py - broadcasting_exercise_10.py
│   └── exception_practice.py
│   └── user_info_formatter.py
│   └── file_automation.py
├── great_expectations/        # Great Expectations project directory
├── day1_plan.md               # Task scope notes
└── .gitignore                 # Excludes venv/, __pycache__/, data exports, etc.
```

---

### 📚 What This Demonstrates

By reviewing or cloning this repository, you'll see a professional-level example of:

1. **Systematic project organization**
2. **Clean, modular, and well-documented Python scripts**
3. **Proficiency in NumPy, Pandas, and file automation**
4. **Advanced Git branching, rebasing, and merge conflict handling**
5. **Robust exception handling strategies**
6. **Data quality checks via Great Expectations**
7. **Effective public documentation and portfolio building**

---

### 🌟 Next Steps

- Integrate **Matplotlib/Seaborn** for visualization of analysis results.
- Extend the ETL scripts to pull real-world APIs and datasets.
- Implement **unit testing** using `pytest` for automation reliability.
- Experiment with **machine learning models** (NumPy-powered regression).

---

