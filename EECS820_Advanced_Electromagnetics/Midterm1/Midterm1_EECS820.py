import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

import matplotlib
matplotlib.rcParams.update({'font.size': 10})
font = {'weight' : 'bold', 'size'   : 10}
matplotlib.rc('font', **font)

# ========================
# Parameters
# ========================
n1 = 1.5       # Core refractive index
n2 = 1.45      # Cladding refractive index
d = 2e-6       # Core thickness (m)
lambda_range = np.linspace(1.0e-6, 2.0e-6, 200)  # 1.0 to 2.0 µm
k0_range = 2*np.pi/lambda_range

# ========================
# TE Modes Calculation
# ========================
def te_eq(beta, k0, m, n1, n2, d):
    kappa = np.sqrt(np.abs((n1*k0)**2 - beta**2))
    gamma = np.sqrt(np.abs(beta**2 - (n2*k0)**2))
    if m % 2 == 0:  # Even modes
        return np.tan(kappa*d/2) - gamma/kappa if kappa != 0 else -np.inf
    else:  # Odd modes
        return 1/np.tan(kappa*d/2) + gamma/kappa if kappa != 0 else np.inf

te_betas = {0: [], 1: [], 2: []}
for k0 in k0_range:
    for m in [0, 1, 2]:
        beta_min = n2*k0 + 1e-6
        beta_max = n1*k0 - 1e-6
        beta_guess = beta_max * (1 - 0.005*(m+1))
        try:
            sol = fsolve(te_eq, beta_guess, args=(k0, m, n1, n2, d), full_output=True)
            if sol[2] == 1 and beta_min < sol[0][0] < beta_max:
                te_betas[m].append(sol[0][0])
            else:
                te_betas[m].append(np.nan)
        except:
            te_betas[m].append(np.nan)

# ========================
# TM Modes Calculation
# ========================
def tm_eq(beta, k0, m, n1, n2, d):
    kappa = np.sqrt(np.abs((n1*k0)**2 - beta**2))
    gamma = np.sqrt(np.abs(beta**2 - (n2*k0)**2))
    if m % 2 == 0:  # Even modes
        return np.tan(kappa*d/2) - (n1**2*gamma)/(n2**2*kappa) if kappa != 0 else -np.inf
    else:  # Odd modes
        return 1/np.tan(kappa*d/2) + (n1**2*gamma)/(n2**2*kappa) if kappa != 0 else np.inf

tm_betas = {0: [], 1: [], 2: []}
for k0 in k0_range:
    for m in [0, 1, 2]:
        beta_min = n2*k0 + 1e-6
        beta_max = n1*k0 - 1e-6
        beta_guess = beta_max * (1 - 0.005*(m+1))
        try:
            sol = fsolve(tm_eq, beta_guess, args=(k0, m, n1, n2, d), full_output=True)
            if sol[2] == 1 and beta_min < sol[0][0] < beta_max:
                tm_betas[m].append(sol[0][0])
            else:
                tm_betas[m].append(np.nan)
        except:
            tm_betas[m].append(np.nan)

# ========================
# Plot: TE and TM modes
# ========================
plt.figure(figsize=(12, 4))

# Panel 1: TE Modes
plt.subplot(1, 2, 1)
colors = ['b', 'g', 'r']
for m in [0, 1, 2]:
    plt.plot(lambda_range*1e6, np.array(te_betas[m])*1e-6, 
             color=colors[m], label=f'TE{m}')
plt.xlabel(r'Wavelength $\lambda$ (µm)')
plt.ylabel('Propagation Constant β (rad/µm)')
plt.title(r'${\bf TE~ Modes}$')
plt.legend()
plt.grid(color = 'gray', lw = 0.5, alpha = 0.25, ls = 'dashed')
plt.axvline(1.3, color='k', linestyle=':', alpha=0.5)  # λ=1.3µm marker

# Panel 2: TM Modes
plt.subplot(1, 2, 2)
for m in [0, 1, 2]:
    plt.plot(lambda_range*1e6, np.array(tm_betas[m])*1e-6, 
             color=colors[m], linestyle='--', label=f'TM{m}')
plt.xlabel(r'Wavelength $\lambda$ (µm)')
plt.title(r'${\bf TM~ Modes}$')
plt.legend()
plt.grid(color = 'gray', lw = 0.5, alpha = 0.25, ls = 'dashed')
plt.axvline(1.3, color='k', linestyle=':', alpha=0.5)  # λ=1.3µm marker

plt.tight_layout()
plt.savefig('dispersion.png', dpi=300, bbox_inches='tight')
plt.show()

# ========================
# Mode Profiles (Ey vs x)
# ========================
k0 = 2*np.pi/1.3e-6  # Fixed wavelength (1.3 µm)
x = np.linspace(-3*d, 3*d, 1000)  # Extended x-range

def te_field(x, beta, m, n1, n2, d):
    kappa = np.sqrt((n1*k0)**2 - beta**2)
    gamma = np.sqrt(beta**2 - (n2*k0)**2)
    A = 1  # Normalization
    core_region = np.abs(x) <= d/2
    cladding_region = np.abs(x) > d/2
    if m % 2 == 0:  # Even mode
        field = np.zeros_like(x)
        field[core_region] = A*np.cos(kappa*x[core_region])
        field[cladding_region] = A*np.cos(kappa*d/2)*np.exp(-gamma*(np.abs(x[cladding_region])-d/2))
    else:  # Odd mode
        field = np.zeros_like(x)
        field[core_region] = A*np.sin(kappa*x[core_region])
        field[cladding_region] = A*np.sign(x[cladding_region])*np.sin(kappa*d/2)*np.exp(-gamma*(np.abs(x[cladding_region])-d/2))
    return field

plt.figure(figsize = (12, 6))
for i, m in enumerate([0, 1, 2]):
    plt.subplot(3, 1, i+1)
    beta_te = fsolve(te_eq, n1*k0*(0.99 - 0.01*m), args=(k0, m, n1, n2, d))[0]
    Ey = te_field(x, beta_te, m, n1, n2, d)
    plt.plot(x*1e6, Ey, 'b-', label=f'TE{m}')
    plt.axvline(-d/2*1e6, color='k', linestyle=':', alpha=0.5)
    plt.axvline(d/2*1e6, color='k', linestyle=':', alpha=0.5)
    plt.ylabel('$E_y$ (a.u.)')
    plt.title(f'TE{m} Mode Profile ($\lambda=1.3\ \mu m$)')
    plt.legend(loc = 'upper right')
    plt.grid(color = 'gray', lw = 0.5, alpha = 0.25, ls = 'dashed')

plt.xlabel('x (µm)')
plt.tight_layout()
plt.savefig('mode_profiles.png', dpi=300, bbox_inches='tight')
plt.show()