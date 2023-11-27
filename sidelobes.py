import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from scipy.special import jn

# Constants
c = 343       # Speed of sound in air in m/s
radius = 0.1  # Radius of the piston in meters (10 cm converted to meters)

# Function to calculate far-field directivity at a given frequency and polar angle
def farfield_directivity(frequency, theta):
    omega = 2 * np.pi * frequency
    k = omega / c
    x = k * radius * np.sin(theta)
    return 20 * np.log10(np.abs(2 * jn(1, x) / x))

# Function to find the frequency that shows two clear sidelobes and the angular width of the main lobe
def find_frequency_and_main_lobe_width():
    # Objective function to maximize the directivity (minimize the negative directivity)
    def objective(frequency):
        theta_values = np.linspace(0, np.pi, 180)
        directivity_values = [farfield_directivity(frequency, theta) for theta in theta_values]
        return -np.min(directivity_values)

    # Use minimize_scalar to find the frequency that maximizes the directivity
    result = minimize_scalar(objective, bounds=(10, 5000), method='bounded')

    if result.success:
        frequency_max_directivity = result.x
        theta_values = np.linspace(0, np.pi, 180)
        directivity_values = [farfield_directivity(frequency_max_directivity, theta) for theta in theta_values]

        # Find the 3 dB down points on the main lobe
        main_lobe_indices = np.where(directivity_values == np.max(directivity_values))[0]
        threshold_directivity = directivity_values[main_lobe_indices[0]] - 3
        main_lobe_indices_3dB = np.where(directivity_values >= threshold_directivity)[0]
        main_lobe_width_rad = theta_values[main_lobe_indices_3dB[-1]] - theta_values[main_lobe_indices_3dB[0]]

        return frequency_max_directivity, np.degrees(main_lobe_width_rad)
    else:
        print("Unable to find a valid solution.")
        return None, None

# Find the frequency and main lobe width
frequency_max_directivity, main_lobe_width = find_frequency_and_main_lobe_width()

# Print the result
if frequency_max_directivity is not None and main_lobe_width is not None:
    print(f"The frequency that shows two clear sidelobes is approximately {frequency_max_directivity:.2f} Hz.")
    print(f"The angular width of the main lobe (3 dB down points) is approximately {main_lobe_width:.2f} degrees.")

    # Plotting
    theta_values = np.linspace(0, np.pi, 180)
    directivity_values = [farfield_directivity(frequency_max_directivity, theta) for theta in theta_values]

    plt.figure(figsize=(8, 6))
    plt.plot(np.degrees(theta_values), directivity_values)
    plt.title('Far-Field Directivity')
    plt.xlabel('Polar Angle (degrees)')
    plt.ylabel('Sound Pressure Level (dB SPL)')
    plt.grid(True)
    plt.show()
else:
    print("Unable to plot the result.")
