# Ahuja Slock

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])

common = []
for i in a:
    if i in b:
        common.append(i)

print(np.array(common))
