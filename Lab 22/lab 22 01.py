# Ahuja Slock
import pandas as pd

csv_file_path = r"C:\Users\OM\OneDrive\Desktop\sample_data.csv"
df_csv = pd.read_csv(csv_file_path)

print("CSV Data:")
print(df_csv)




import pandas as pd

df_csv = pd.read_csv(r"C:\Users\OM\OneDrive\Desktop\sample_data.csv")

filtered_data = df_csv[df_csv['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered_data)




json_file_path = r"C:\Users\OM\OneDrive\Desktop\sample_data.json"   # correct full path
df_json = pd.read_json(json_file_path)

# Display the DataFrame
print("\nJSON Data:")
print(df_json)

average_age = df_json['Age'].mean()
print("\nAverage Age:", average_age)

import pandas as pd

csv_file_path = r"C:\Users\OM\OneDrive\Desktop\sample_data.csv"
df_csv = pd.read_csv(csv_file_path)

print("\nCSV Data:")
print(df_csv)

excel_file_path = r"C:\Users\OM\OneDrive\Desktop\sample_data.xlsx"
df_excel = pd.read_excel(excel_file_path)

print("\nExcel Data:")
print(df_excel)

# Count the number of entries in Excel
entry_count = df_excel.shape[0]
print("\nNumber of entries in Excel file:", entry_count)


filtered_data.to_csv(r"C:\Users\OM\OneDrive\Desktop\filtered_data.csv", index=False)
print("\nFiltered data saved to 'filtered_data.csv'.")

# Save DataFrame to a new JSON file
df_json.to_json(r"C:\Users\OM\OneDrive\Desktop\new_data.json", orient='records', lines=True)
print("JSON data saved to 'new_data.json'.")

# Save DataFrame to a new Excel file
df_excel.to_excel(r"C:\Users\OM\OneDrive\Desktop\new_data.xlsx", index=False)
print("Excel data saved to 'new_data.xlsx'.")
