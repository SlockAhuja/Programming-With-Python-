# AHuja slock

import sympy as sp

# Define symbols
n, z = sp.symbols('n z')

# Define the sequence x[n] = 3*n*u[n]
x_n = 3 * n

# Compute the Z-transform (sum from n=0 to ∞)
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = 3n u[n]:")
sp.pprint(X_z.simplify(), use_unicode=True)
