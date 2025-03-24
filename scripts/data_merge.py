import pandas as pd
from pathlib import Path
from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.data_context import get_context




# Load raw CSVs
column_names = ['client_id', 'purchase_date', 'item', 'quantity', 'price']

df_q1 = pd.read_csv('../data/sales_q1.csv', encoding='latin1', names=column_names, header=None, sep=',')
df_q2 = pd.read_csv('../data/sales_q2.csv', encoding='latin1', names=column_names, header=None, sep=',')
df_q3 = pd.read_csv('../data/sales_q3.csv', encoding='latin1', names=column_names, header=None, sep=',')

# Merge
merged_df = pd.concat([df_q1, df_q2, df_q3])

# Drop duplicates
merged_df.drop_duplicates(subset=['client_id', 'purchase_date', 'item'], inplace=True)

# Sort
merged_df.sort_values(by='purchase_date', inplace=True)

# Export consolidated CSV
output_path = Path('../data/sales_consolidated.csv')
merged_df.to_csv(output_path, index=False)
print(f"Merged dataset saved to {output_path.resolve()}")

# ----------- Validation Part -----------


# Load GE context
context = get_context()

# Directly get validator from Pandas DataFrame
validator = context.sources.pandas_default.read_dataframe(merged_df)