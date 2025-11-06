# AHuja SLock

import sympy as sp

# Define symbols
n, z, omega = sp.symbols('n z omega')

# Define the sequence x[n] = cos(omega*n)*u[n]
x_n = sp.cos(omega * n)

# Compute the Z-transform
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("\nZ-transform of x[n] = cos(omega*n) u[n]:")
sp.pprint(sp.simplify(X_z), use_unicode=True)
