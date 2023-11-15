import numpy as np
import matplotlib.pyplot as plt

zetta_range = np.linspace(0, 10, 100)

R_values = np.zeros_like(zetta_range)
T_values = np.zeros_like(zetta_range)
Ri_values = np.zeros_like(zetta_range)
Ti_values = np.zeros_like(zetta_range)

for i, zetta in enumerate(zetta_range):
    R = (zetta - 1) / (zetta + 1)
    T = 2 * zetta / (zetta + 1)
    Ri = np.abs(R)**2
    Ti = 1 - Ri
    R_values[i] = R
    T_values[i] = T
    Ri_values[i] = Ri
    Ti_values[i] = Ti

plt.figure()
plt.plot(zetta_range, R_values, linewidth=2, label='R')
plt.plot(zetta_range, T_values, linewidth=2, label='T')
plt.plot(zetta_range, Ri_values, linewidth=2, label='Ri')
plt.plot(zetta_range, Ti_values, linewidth=2, label='Ti')
plt.xlabel('(r2/r1)')
plt.title('Reflection and Transmission Coefficients vs. zetta (r2/r1)')
plt.legend()
plt.grid(True)
plt.show()
