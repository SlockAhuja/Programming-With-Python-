# AHuja Slock 

import pandas as pd

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

# Vertical stack
print("Vertical stack:")
print(s1.append(s2))  # simple and easy

# Horizontal stack
print("\nHorizontal stack:")
df = pd.DataFrame({'s1': s1, 's2': s2})
print(df)
