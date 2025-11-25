# Ahuja Slock

import pandas as pd

csv_file_path = r"C:\Users\OM\OneDrive\Desktop\sample_data.csv"
df_csv = pd.read_csv(csv_file_path)

df_demo = df_csv.copy()

# Introduce missing value manually (optional demonstration)
df_demo.loc[1, 'Age'] = None

print("\nBefore Filling Missing Values:")
print(df_demo)

# Calculate mean of the column (ignores missing values)
mean_age = df_demo['Age'].mean()

# Fill missing values
df_demo['Age'] = df_demo['Age'].fillna(mean_age)

print("\nAfter Filling Missing Values (Age filled with mean):")
print(df_demo)
