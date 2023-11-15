import numpy as np
import matplotlib.pyplot as plt

rho = 1.2
c = 343
L = 0.025
frequency_range = np.arange(1, 20000, step=0.05)
kL = 2 * np.pi * frequency_range * L / c


gamma_normal = 1 - (((rho * c * (1/np.tan(kL)))**2 + (rho * c * (np.cos(0) - 1))**2 ) / (((rho * c * (1/np.tan(kL)))**2) + (rho * c * (np.cos(0) + 1))**2))
gamma_60_deg = 1 - (((rho * c * (1/np.tan(kL)))**2 + (rho * c * (np.cos(np.radians(60)) - 1))**2) / (((rho * c * (1/np.tan(kL)))**2) + (rho * c * (np.cos(np.radians(60)) + 1))**2))

plt.figure(figsize=(10, 6))
plt.plot(frequency_range, gamma_normal, label='Normal Incidence')
plt.plot(frequency_range, gamma_60_deg, label='60-Degree Incidence')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Absorption Coefficient')
plt.title('Absorption Coefficient vs Frequency')
plt.legend()
plt.grid(True)
plt.savefig("output.jpg")
plt.show()
