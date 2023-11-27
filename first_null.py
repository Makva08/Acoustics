import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import jn, struve

# Constants
rho_0 = 1.21  # Air density in kg/m^3
c = 343  # Speed of sound in air in m/s
radius = 0.1  # Radius of the piston in meters (10 cm converted to meters)

def radiation_impedance(r, frequency):
    omega = 2 * np.pi * frequency
    k = omega / c
    x = k * r
    R_x = 1 - 2 * jn(1, x) / x  # Radiation resistance term
    X_x = 2 * struve(1,x) / x          # Radiation reactance term (Struve function)
    Z = rho_0 * c * np.pi * radius**2 * (R_x + 1j * X_x)
    return Z

def find_first_null_frequency():
    def objective(frequency):
        theta_null = np.radians(90)
        return np.abs(radiation_impedance(frequency, theta_null))
    result = minimize_scalar(objective, bounds=(10, 5000), method='bounded')
    frequency_null = result.x
    return frequency_null

frequency_first_null = find_first_null_frequency()
print(f"The frequency at the first null (90 degrees) is approximately {frequency_first_null:.2f} Hz.")

