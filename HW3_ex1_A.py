import numpy as np
import matplotlib.pyplot as plt

f1 = 500
f2 = 1000
c = 343
wl1 = c / f1
wl2 = c / f2

pos = np.linspace(0, 2 * wl2, 1000)

Prms1 = np.sqrt(0.8 - 0.48 * np.cos(2 * np.pi * pos / wl1))
Prms2 = np.sqrt(0.8 - 0.48 * np.cos(2 * np.pi * pos / wl2))

Urms1 = Prms1 / 3.43
Urms2 = Prms2 / 3.43

plt.figure()
plt.plot(pos, Prms1, 'b', linewidth=2, label='500 Hz')
plt.plot(pos, Prms2, 'r', linewidth=2, label='1000 Hz')
plt.plot(pos, Urms1, 'b--', linewidth=2, label='500 Hz (Urms)')
plt.plot(pos, Urms2, 'r--', linewidth=2, label='1000 Hz (Urms)')
plt.xlabel('Position in Tube (m)')
plt.ylabel('Mean Square Pressure')
plt.title('Mean Square Pressure in a Tube')
plt.legend()
plt.grid(True)

print('Wavelengths:')
print(f'500 Hz: {wl1:.4f} m')
print(f'1000 Hz: {wl2:.4f} m')

plt.show()
