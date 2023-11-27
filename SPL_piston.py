import numpy as np
import matplotlib.pyplot as plt

rho = 1.21  # medium = air
c = 343
freqs = [100, 1000, 10000]
radius = 0.1
velocity_amplitude = 0.002
Pref=20e-6

SPLs = []

# piston operating in rigid baffle, Kinsler et al. (7.4.4)
# dist - radial distance from the source;   t - time
def sound_pressure(dist, frequency, radius, velocity_amplitude, time):
    omega = 2 * np.pi * frequency
    k = omega / c
    term = 1 - np.exp(-1j * k * (np.sqrt(dist ** 2 + radius ** 2) - dist))
    P_calc = rho * c * velocity_amplitude * term * np.exp(1j * (omega * time - k * dist))
    return P_calc

distances = np.logspace(-3, 3, 1000)

for frequency in freqs:
    Prms_values = [np.abs(sound_pressure(r, frequency, radius, velocity_amplitude, time=0)) for r in distances]
    SPL = 20 * np.log10(np.array(Prms_values) / Pref)
    SPLs.append(SPL)

plt.figure(figsize=(10, 6))
for i, frequency in enumerate(freqs):
    plt.plot(np.log10(distances)*10**3, SPLs[i], label=f'{frequency} Hz')

plt.title('On-axis SPL vs. log10(Distance)')
plt.xlabel('log10(Distance) (m)')
plt.ylabel('Sound Pressure Level (dB SPL)')
plt.legend()
plt.grid(True)
plt.show()
