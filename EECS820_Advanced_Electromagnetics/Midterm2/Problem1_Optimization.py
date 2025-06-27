import numpy as np
from scipy.optimize import minimize

# Given values
n_substrate = 3.55  # Refractive index of GaAs
theta_deg = 20  # Angle of incidence in degrees
theta_rad = np.radians(theta_deg)  # Convert angle to radians

# Function to calculate reflection coefficients for both TE and TM polarizations at 20° angle of incidence
def reflection_error(params):
    # Extract the refractive index and thickness from the parameters
    n_film_opt, d_film_opt = params
    
    # Recalculate the transmitted angle using Snell's law for the optimized n_film
    theta_t_opt = np.arcsin(n_film_opt * np.sin(theta_rad) / n_substrate)
    
    # Calculate reflection coefficients for TE and TM polarizations
    R_TE_opt = np.abs((n_film_opt * np.cos(theta_rad) - n_substrate * np.cos(theta_t_opt)) /
                      (n_film_opt * np.cos(theta_rad) + n_substrate * np.cos(theta_t_opt)))**2
    
    R_TM_opt = np.abs((n_film_opt * np.cos(theta_t_opt) - n_substrate * np.cos(theta_rad)) /
                      (n_film_opt * np.cos(theta_t_opt) + n_substrate * np.cos(theta_rad)))**2
    
    # Sum of errors for both TE and TM reflection coefficients (we want this sum to be minimized)
    return R_TE_opt + R_TM_opt

# Initial guess for refractive index and thickness
initial_guess = [1.88, 130.03]  # Starting with previous values

# Perform the optimization
result = minimize(reflection_error, initial_guess, bounds=[(1.0, 3.0), (50, 500)])

# Extract the optimized refractive index and thickness
optimized_n_film = result.x[0]
optimized_d_film = result.x[1]

# Print the optimized values and the error from the optimization
print("Optimized refractive index:", optimized_n_film)
print("Optimized thickness:", optimized_d_film, "nm")
print("Optimization error (sum of reflection coefficients):", result.fun)