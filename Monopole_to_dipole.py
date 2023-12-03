import numpy as np
import matplotlib.pyplot as plt

rho_0 = 1.21
c = 343
S = 0.05
angle_dipole = 60

def reduction_in_spl(frequency):
    k = 2 * np.pi * frequency / c
    reduction_in_SPL = 20 * np.log10(np.abs(k*S*np.cos(angle_dipole)))
    return reduction_in_SPL

max_kS = 0.05
# 2pi*f*S/c=0.05 -> 2pi*f/c=1
frequencies = np.linspace(10, c / (2 * np.pi ), 1000)

reduction_spl_values = [reduction_in_spl(frequency) for frequency in frequencies]
plt.figure(figsize=(10, 6))
plt.plot(frequencies, reduction_spl_values, label=f'Reduction in SPL (Angle: {angle_dipole} degrees)')
plt.title('Reduction in SPL for Monopole to Dipole Conversion')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Reduction in SPL (dB)')
plt.legend()
plt.grid(True)
plt.show()
