# A rigid piston of 10 cm radius is operating in rigid baffle at different frequencies
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.special import j1, struve  # j1 = Bessel function - first order
import sympy as sp

x = sp.symbols('x')
rho = 1.21  # medium = air
c = 343
freqs = [100, 1000, 10000]
radius = 0.1
velocity_amplitude = 0.002
Pref=20e-6

SPLs = []

def find_local_maxima(x, y, threshold=0):
    peaks, _ = find_peaks(y, height=threshold)
    maxima_x = x[peaks]
    maxima_y = y[peaks]
    return maxima_x, maxima_y

# dist - radial distance from the source;   t - time
def sound_pressure(dist, frequency, radius, velocity_amplitude, time):
    omega = 2 * np.pi * frequency
    k = omega / c
    term = 1 - np.exp(-1j * k * (np.sqrt(dist ** 2 + radius ** 2) - dist))
    P_calc = rho * c * velocity_amplitude * term * np.exp(1j * (omega * time - k * dist))
    return P_calc

def farfield_directivity(theta, frequency):
    omega = 2 * np.pi * frequency
    k = omega / c
    r = 0.1
    term1 = 2 * j1(k * r * np.sin(theta))
    term2 = k * r * np.sin(theta)
    SPL = 20 * np.log10(np.abs(term1 / term2))
    return SPL

def radiation_impedance(r, frequency):
    omega = 2 * np.pi * frequency
    k = omega / c
    x = k * r
    R_x = 1 - ((2 * j1(2*x)) / (2*x))
    # X_x = 2 * struve(1,x) / x
    Z=rho * c * np.pi * radius**2 * (R_x)
    return Z

def radiated_sound_power(frequency):
    r = 0.1
    Z_r = radiation_impedance(r, frequency)
    power = np.real((Z_r * velocity_amplitude**2) / 2)
    return power


# Clculating the radiated sound power using rad. impedance
for frequency in freqs:
    power = radiated_sound_power(frequency)
    print(f"At {frequency} Hz: {power:.8f} Watts")

distances = np.logspace(-3, 3, 1000)
theta_values = np.linspace(-(np.pi / 2), np.pi / 2, 1000)  # Polar angle values from 0 to pi radians

# Loop identifies extent of the nearfield in each case -
# dist from src at which  the spatial variation with distance transitions to a simple (1/r) decay
for frequency in freqs:
    Prms_values = [np.abs(sound_pressure(r, frequency, radius, velocity_amplitude, time=0)) for r in distances]
    SPL = 20 * np.log10(np.array(Prms_values) / Pref)
    SPLs.append(SPL)
    maxima_x, maxima_y = find_local_maxima(distances, SPL)
    print(maxima_y)

# Loop finds first null of Bessel function
for f in freqs:
    eqn = 2 * np.pi * (f / 343) * 0.1 * sp.sin(x) - 3.8317
    soln = sp.solve(eqn, x)
    print("Solutions for the first null:", soln)

# Plots SPL's of piston at diff freqs over distance
plt.figure(1, figsize=(10, 6))
for i, frequency in enumerate(freqs):
    plt.semilogx(distances, SPLs[i], label=f'{frequency} Hz')
plt.title('On-axis SPL vs. log10(Distance)')
plt.xlabel('log10(Distance) (m)')
plt.ylabel('Sound Pressure Level (dB SPL)')
plt.legend()
plt.grid(True)
plt.show()

# Plots farfield directivity
plt.figure(2, figsize=(10, 6))
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

# Finding and ploting a result showing two clear sidelobes
# 2 sidelobes means J1(j3m) which is 3rd zero of Bessel function
# 3rd zero of Bessel function = 10.1735
k2=10.1735/0.1
f=k2*c/(2*np.pi)
print(f)

plt.figure(3, figsize=(10, 6))
SPL_value = [farfield_directivity(theta, f) for theta in theta_values]
plt.plot(np.degrees(theta_values), SPL_value, label=f'{f} Hz')
plt.show()