# 📄 Day 1 Plan — Sales CSV Consolidation & Validation

## 🟢 Objective
Consolidate three separate CSV sales datasets into one clean, structured dataset using Pandas, ensuring data quality and consistency via automated validation with Great Expectations.

---

## 📂 Input Files
Located in `/data` directory:
- `sales_q1.csv` — Sales data for Q1.
- `sales_q2.csv` — Sales data for Q2.
- `sales_q3.csv` — Sales data for Q3.

**Each CSV contains:**
| Column Name    | Data Type | Description                      |
|---------------|----------|----------------------------------|
| `client_id`    | string    | Unique client identifier         |
| `purchase_date`| YYYY-MM-DD| Date of transaction              |
| `item`         | string    | Item purchased                   |
| `quantity`     | integer   | Quantity purchased               |
| `price`        | float     | Price per item                   |

---

## 🛠️ Requirements
- **Pandas Tasks:**
  - Load each CSV file.
  - Verify column consistency across all files.
  - Concatenate datasets into one unified DataFrame.
  - Remove duplicates based on `client_id`, `purchase_date`, `item`.
  - Sort by `purchase_date` ascending.
  - Export merged dataset as `/data/sales_consolidated.csv`.

- **Great Expectations Tasks:**
  - Initialize Great Expectations project (if not yet done).
  - Create expectation suite `sales_merge_suite`:
    - Validate existence and datatypes of all columns.
    - Ensure no null values in `client_id`, `purchase_date`, `item`.
    - Check `quantity` > 0 and `price` > 0.
    - Validate `purchase_date` follows `YYYY-MM-DD` format.
  - Run validation after merging.

---

## 📑 Implementation Steps

1. **Branch Setup**
   ```bash
   git checkout -b feature/sales-data-merge
