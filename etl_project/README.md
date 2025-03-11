# Mini ETL Pipeline for Data Processing
## Description
This project implements a basic ETL (Extract, Transform, Load) pipeline using Python. 
It extracts raw data from a CSV file, transforms it by cleaning, filtering, and structuring key values, 
and loads the processed data into a new CSV file for further analysis.
## Features
- Reads and extracts raw data from a CSV file.
- Cleans missing or incorrect values in key fields.
- Filters out incomplete records for accuracy.
- Transforms and aggregates key insights.
- Outputs a structured CSV file for further analysis.
## Project Structure
📂 etl_project
 ├── raw_data.csv           # Input dataset
 ├── processed_data.csv      # Output processed dataset
 ├── mini_etl.py            # Main ETL script
 ├── README.md              # Project documentation
## Installation & Setup
1. Clone the repository: git clone <repository-url> cd etl_project
2. Install dependencies: pip install pandas
3. Run the script: python mini_etl.py
4. Check the generated `processed_data.csv` file for results.
## Usage
- **Step 1:** Ensure `raw_data.csv` is in the same directory.
- **Step 2:** Run `mini_etl.py` to process the data.
- **Step 3:** The output will be saved in `processed_data.csv`.
## Data Processing Steps
The ETL script performs the following steps:
1. **Extract**: Reads `raw_data.csv` into a structured format.
2. **Transform**:
   - Cleans missing values in `Age` and `Salary`.
   - Filters out records with incomplete or invalid data.
   - Standardizes the formatting of numerical fields.
3. **Load**: Saves the cleaned dataset into `processed_data.csv` for further use.
## Example Output (processed_data.csv)
Name,Age,Salary,Department
Alice,30,55000,Engineering
Bob,40,72000,Marketing
Charlie,25,48000,Sales
David,35,63000,Finance
Frank,50,95000,Engineering
Grace,45,82000,Marketing
Ian,32,70000,Finance
Jack,38,68000,HR
## Future Improvements
- Implement error handling for invalid CSV formats.
- Add logging for better debugging.
- Allow users to specify input and output filenames dynamically.
