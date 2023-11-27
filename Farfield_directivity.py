import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j1  # Bessel function

rho = 1.21  # medium = air
c = 343
freqs = [100, 1000, 10000]
radius = 0.1
velocity_amplitude = 0.002
Pref=20e-6

def farfield_directivity(theta, frequency):
    omega = 2 * np.pi * frequency
    k = omega / c
    r = 10
    term1 = 2 * j1(k * r * np.sin(theta))
    term2 = k * r * np.sin(theta)
    SPL = 20 * np.log10(np.abs(term1 / term2))
    return SPL

theta_values = np.linspace(-(np.pi / 2), np.pi / 2, 1000)  # Polar angle values from 0 to pi radians

plt.figure(figsize=(10, 6))
for frequency in freqs:
    SPL_values = [farfield_directivity(theta, frequency) for theta in theta_values]
    plt.plot(np.degrees(theta_values), SPL_values, label=f'{frequency} Hz')

plt.title('Far-Field Directivity of a Rigid Piston')
plt.xlabel('Polar Angle (degrees)')
plt.ylabel('Sound Pressure Level (dB SPL)')
plt.xlim([-90, 90])
plt.legend()
plt.grid(True)
plt.show()
