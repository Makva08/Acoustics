import numpy as np
import matplotlib.pyplot as plt

h = 1
n = np.arange(1, 4, 1)
t = np.linspace(0, 2 * np.pi, 1000)

y1 = (8 * h) / (n[0]**2 * np.pi**2) * np.sin(np.pi * n[0] / 2) * np.sin(n[0] * t)
y2 = (8 * h) / (n[1]**2 * np.pi**2) * np.sin(np.pi * n[1] / 2) * np.sin(n[1] * t)
y3 = (8 * h) / (n[2]**2 * np.pi**2) * np.sin(np.pi * n[2] / 2) * np.sin(n[2] * t)
linear_combination = y1 + y2 + y3

plt.figure()

plt.subplot(4, 1, 1)
plt.plot(t, y1, 'b', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('First Harmonic')
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t, y2, 'r', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Second Harmonic')
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, y3, 'g', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Third Harmonic')
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t, linear_combination, 'm', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Linear Combination')
plt.grid(True)
plt.ylim([-3, 3])

plt.suptitle('Waveforms of Individual Harmonics and Linear Combination')
plt.show()
