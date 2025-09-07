# AHuja Slock 

import pandas as pd
import numpy as np

# 1. From a list
my_list = [10, 20, 30, 40]
s1 = pd.Series(my_list)
print("Series from list:\n", s1, "\n")

# 2. From a NumPy array
my_array = np.array([50, 60, 70, 80])
s2 = pd.Series(my_array)
print("Series from NumPy array:\n", s2, "\n")

# 3. From a dictionary
my_dict = {'a': 100, 'b': 200, 'c': 300}
s3 = pd.Series(my_dict)
print("Series from dictionary:\n", s3)
