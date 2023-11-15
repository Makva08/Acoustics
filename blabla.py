from sympy import Matrix, symbols, solve, I, exp

k1, x, k2, k3, r = symbols("k1 x k2 k3 r")
R, T, A, B = symbols('R T A B')

# Define the system of equations
f1 = k1*(exp(-I*k1*x) + R*exp(I*k1*x)) - k2*(A*exp(-I*k2*x) + B*exp(I*k2*x))
f2 = k2*(A*exp(-I*k2*x) + B*exp(I*k2*x) - k3*T*exp(-I*k3*x))
f3 = exp(-I*k1*x) + R*exp(I*k1*x) - A*exp(-I*k2*x) - B*exp(I*k2*x) + (1/r)*k1*(exp(-I*k1*x) + R*exp(I*k1*x))
f4 = A*exp(-I*k2*x) + B*exp(I*k2*x) - T*exp(-I*k3*x) + (1/r)*k3*T*exp(-I*k3*x)

# Solve the system of equations
sol = solve([f1, f2, f3, f4], [R, T, A, B])
