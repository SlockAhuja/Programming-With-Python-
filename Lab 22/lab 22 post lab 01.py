# Ahuja Slock

import pandas as pd

csv_file_path = r"C:\Users\OM\OneDrive\Desktop\sample_data.csv"
df_csv = pd.read_csv(csv_file_path)

# Post Lab 1: Check data types of each column
print("\nData Types of Each Column:")
print(df_csv.dtypes)
