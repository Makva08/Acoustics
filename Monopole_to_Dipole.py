import numpy as np
import matplotlib.pyplot as plt

rho_0 = 1.21
c = 343
S = 0.05
angle_dipole = 60

# radiation impedance for a monopole
def radiation_impedance_monopole(frequency):
    k = 2 * np.pi * frequency / c
    Z_m = rho_0 * c * S * (1 - 1j / (k * S))
    return Z_m

# radiation impedance for a dipole (at an angle)
def radiation_impedance_dipole(frequency, angle):
    k = 2 * np.pi * frequency / c
    Z_d = rho_0 * c * S * (1 - 1j / (k * S) * np.cos(np.radians(angle)))
    return Z_d

# reduction in SPL
def reduction_in_spl(frequency):
    Z_m = radiation_impedance_monopole(frequency)
    Z_d = radiation_impedance_dipole(frequency, angle_dipole)
    reduction_in_SPL = 20 * np.log10(np.abs(Z_d / Z_m))
    return reduction_in_SPL

max_kS = 0.05
frequencies = np.linspace(10, c / (2 * np.pi * max_kS), 1000)

reduction_spl_values = [reduction_in_spl(frequency) for frequency in frequencies]
plt.figure(figsize=(10, 6))
plt.plot(frequencies, reduction_spl_values, label=f'Reduction in SPL (Angle: {angle_dipole} degrees)')
plt.title('Reduction in SPL for Monopole to Dipole Conversion')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Reduction in SPL (dB)')
plt.legend()
plt.grid(True)
plt.show()
