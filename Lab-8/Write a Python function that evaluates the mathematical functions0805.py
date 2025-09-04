#Ahuja Slock

import math

def evaluate(x):
    f  = math.cos(2*x)
    f1 = -2*math.sin(2*x)
    f2 = -4*math.cos(2*x)
    return f, f1, f2

print(evaluate(math.pi))
