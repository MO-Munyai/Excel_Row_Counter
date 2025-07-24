
import pandas as pd

# Load the Excel file
df = pd.read_excel('file_name.xlsx')

# Count rows that have at least one non-empty value
non_empty_rows = df.dropna(how='all').shape[0]

print(f"Number of rows with at least one value: {non_empty_rows}")
