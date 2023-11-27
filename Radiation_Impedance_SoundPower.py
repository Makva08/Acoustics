import numpy as np
from scipy.special import jn, struve

rho = 1.21  # medium = air
c = 343
freqs = [100, 1000, 10000]
radius = 0.1
velocity_amplitude = 0.002
Pref=20e-6

# Function to calculate radiation impedance for a piston in a rigid baffle
def radiation_impedance(r, frequency):
    omega = 2 * np.pi * frequency
    k = omega / c
    x = k * r
    R_x = 1 - 2 * jn(1, x) / x  # Radiation resistance term
    X_x = 2 * struve(1,x) / x          # Radiation reactance term (Struve function)
    Z=rho * c * np.pi * radius**2 * (R_x + 1j * X_x)
    return Z

# Function to calculate radiated sound power
def radiated_sound_power(frequency):
    r = 10
    Z_r = radiation_impedance(r, frequency)
    power = np.real((rho * c * Z_r * velocity_amplitude**2) / 2)
    return power

# Calculate and print radiated sound power at specified frequencies
for frequency in freqs:
    power = radiated_sound_power(frequency)
    print(f"At {frequency} Hz: {power:.4f} Watts")
