import numpy as np
from sympy import symbols, Eq, solve
x, y = symbols('x y')
complex_number = x+y*1j
abs_number = abs(complex_number)
print(abs_number)