# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 14:12:42 2025

@author: slock
"""

# Modulus operations
x = 8
y = 3
mod = x % y
print("x % y =", mod)

a = -5
b = 2
res1 = a % b
print("a % b =", res1)

m = 5
n = -2
res2 = m % n
print("m % n =", res2)

e = -5
f = -2
res3 = e % f
print("e % f =", res3)

# Order of precedence
print("((5 + 4) / 3) * 2 =", ((5 + 4) / 3) * 2)

x = 3
y = 4
z = 6
print("x * y // z =", x * y // z)
print("x * (y // z) =", x * (y // z))

x = 2
y = 3
z = 2
print("x ** y ** z =", x ** y ** z)       # Exponentiation is right-to-left
print("(x ** y) ** z =", (x ** y) ** z)
