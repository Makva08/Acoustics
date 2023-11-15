# This is the code for double rigid panel case, in which first wave starts as a unit amplitude
from sympy import symbols, solve, exp

k1, x, k2, k3, r = symbols("k1 x k2 k3 r")
R, T, A, B = symbols('R T A B')

f1 = k1*(exp(-1j*k1*x) + R*exp(1j*k1*x)) - k2*(A*exp(-1j*k2*x) + B*exp(1j*k2*x))
f2 = k2*(A*exp(-1j*k2*x) + B*exp(1j*k2*x) - k3*T*exp(-1j*k3*x))
f3 = exp(-1j*k1*x) + R*exp(1j*k1*x) - A*exp(-1j*k2*x) - B*exp(1j*k2*x) + (1/r)*k1*(exp(-1j*k1*x) + R*exp(1j*k1*x))
f4 = A*exp(-1j*k2*x) + B*exp(1j*k2*x) - T*exp(-1j*k3*x) + (1/r)*k3*T*exp(-1j*k3*x)

sol = solve([f1, f2, f3, f4], [R, T, A, B])

print("Solution:")
print(sol)
