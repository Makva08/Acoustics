import numpy as np
import matplotlib.pyplot as plt

A = 1
k = 1
m = 1
w0 = np.sqrt(k/m)

x0_values = np.array([0, 0, -A, A/2])
v_values = np.array([0, (w0*A)/2, w0*A, (w0*A)*np.sqrt(3)/2])

t = np.linspace(0, 10, 1000)

plt.figure(1)
plt.title('Displacement of Mass-Spring System')
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.grid(True)

for k in range(4):
    v = v_values[k]
    x0 = x0_values[k]
    x = x0 * np.cos(w0 * t) + (v / w0) * np.sin(w0 * t)
    plt.plot(t, x, label=chr(97+k))

plt.legend()
plt.show()

for k in range(4):
    v = v_values[k]
    x0 = x0_values[k]
    x = x0 * np.cos(w0 * t) + (v / w0) * np.sin(w0 * t)

    plt.figure()
    plt.plot(t, x)
    plt.xlabel('Time')
    plt.ylabel('Displacement')
    plt.title(f'Displacement for case {chr(97+k)}')
    plt.grid(True)
    plt.show()
