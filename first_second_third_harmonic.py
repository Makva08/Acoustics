import numpy as np
import matplotlib.pyplot as plt

h = 1
n = np.array([1, 2, 3])

A1 = (8 * h) / (1**2 * np.pi**2) * np.sin(np.pi * 1 / 2)
A2 = (8 * h) / (2**2 * np.pi**2) * np.sin(np.pi * 2 / 2)
A3 = (8 * h) / (3**2 * np.pi**2) * np.sin(np.pi * 3 / 2)

t = np.linspace(0, 2 * np.pi, 1000)
y1 = A1 * np.sin(n[0] * t)
y2 = A2 * np.sin(n[1] * t)
y3 = A3 * np.sin(n[2] * t)

y1_normalized = y1 / h
y2_normalized = y2 / h
y3_normalized = y3 / h

L = 2 * np.pi
x_normalized = t / L

plt.figure()
plt.plot(x_normalized, y1_normalized, 'b', linewidth=2, label='First Harmonic')
plt.plot(x_normalized, y2_normalized, 'r', linewidth=2, label='Second Harmonic')
plt.plot(x_normalized, y3_normalized, 'g', linewidth=2, label='Third Harmonic')
plt.xlabel('x / L')
plt.ylabel('y / h')
plt.title('Normalized First, Second, and Third Harmonics')
plt.legend()
plt.grid(True)
plt.ylim([-2, 2])

linear_combination = y1 + y2 + y3
linear_combination_normalized = linear_combination / h

plt.figure()
plt.plot(x_normalized, linear_combination_normalized, 'm', linewidth=2, label='Linear Combination')
plt.xlabel('x / L')
plt.ylabel('y / h')
plt.title('Normalized Linear Combination')
plt.grid(True)
plt.show()
