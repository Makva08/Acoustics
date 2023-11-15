import numpy as np
import matplotlib.pyplot as plt

kl_fundamental = 2.042
kl_overtone = 4.915
omega_fundamental = kl_fundamental
omega_overtone = kl_overtone
t = np.linspace(0, 2*np.pi, 1000)
fundamental_signal = np.sin(omega_fundamental * t)
overtone_signal = np.sin(omega_overtone * t)

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(t, fundamental_signal, 'b')
plt.xlim([0, 2])
plt.title('Fundamental')

plt.subplot(2, 1, 2)
plt.plot(t, overtone_signal, 'r')
plt.xlim([0, 2])
plt.title('First Overtone')

plt.grid(True)
plt.show()
