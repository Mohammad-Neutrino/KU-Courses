import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({'font.size': 12})
font = {'weight' : 'bold', 'size'   : 12}
matplotlib.rc('font', **font)

# Given values
n_film = 1.88  # Refractive index of the film
n_substrate = 3.55  # Refractive index of GaAs

# Case 1: Wavelength range (900-1060 nm) at normal incidence
wavelengths = np.linspace(900, 1060, 100)  # Wavelengths from 900 nm to 1060 nm
R_wavelength = (n_film - n_substrate)**2 / (n_film + n_substrate)**2  # Reflection for normal incidence

# Case 2: Angle of incidence range (0° to 45°) at 980 nm for TE and TM polarizations
angles_deg = np.linspace(0, 45, 100)  # Angles from 0° to 45°
angles_rad = np.radians(angles_deg)  # Convert angles to radians

# Snell's law to compute the transmitted angle
theta_t = np.arcsin(n_film * np.sin(angles_rad) / n_substrate)

# TE and TM reflection coefficients
R_TE = (n_film * np.cos(angles_rad) - n_substrate * np.cos(theta_t)) / (n_film * np.cos(angles_rad) + n_substrate * np.cos(theta_t))
R_TM = (n_film * np.cos(theta_t) - n_substrate * np.cos(angles_rad)) / (n_film * np.cos(theta_t) + n_substrate * np.cos(angles_rad))

# Plotting the results
fig, ax = plt.subplots(2, 1, figsize = (12, 7))

# Plot for Case 1: Reflection vs Wavelength
ax[0].plot(wavelengths, np.full_like(wavelengths, R_wavelength), color = 'b')
ax[0].set_xlabel("Wavelength (nm)")
ax[0].set_ylabel("Reflectance")
ax[0].grid(color = 'k', ls = 'dashed', lw = 0.25, alpha = 0.25)

# Plot for Case 2: Reflection vs Angle of Incidence for TE and TM polarizations
ax[1].plot(angles_deg, R_TE**2, label = "TE Polarization", color = 'teal')
ax[1].plot(angles_deg, R_TM**2, label = "TM Polarization", color = 'salmon')
ax[1].set_xlabel("Angle of Incidence (°)")
ax[1].set_ylabel("Reflectance")
ax[1].legend()
ax[1].grid(color = 'k', ls = 'dashed', lw = 0.25, alpha = 0.25)

plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS820_Advanced_Electromagnetics_Spring2025/EECS820_Advanced_Electromagnetics/Midterm2/reflection_angle_wavelength.png', dpi = 400)
plt.tight_layout()
plt.show()
