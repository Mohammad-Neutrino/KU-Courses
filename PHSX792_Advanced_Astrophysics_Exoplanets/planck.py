import numpy as np
import matplotlib.pyplot as plt

h = 6.626*10**(-34)
k = 1.38*10**(-23)
c = 3*10**8

lambp = 2.898
lambs = 2.898/5.778

lam = np.linspace(0.3e-6, 3e-6, 100)
freq = c/lam

Tp, Rp = 1000.0, 71492
Ts, Rs = 5778.0, 695700

A = 2*h*pow(c, 2)
powerp = h*c/(k*lam*Tp)
powers = h*c/(k*lam*Ts)

Bp = (A/pow(lam, 5))*(1./(np.exp(powerp) - 1.))
Bs = (A/pow(lam, 5))*(1./(np.exp(powers) - 1.))

yerrorp = [np.std(Bp)/np.sqrt(len(Bp))]*len(Bp)
yerrors = [np.std(Bs)/np.sqrt(len(Bs))]*len(Bs)

ratio = (Bp/Bs)*(Rp/Rs)**2
yerrorr = [np.std(ratio)/np.sqrt(len(ratio))]*len(ratio)

fig, ax = plt.subplots(figsize = (10, 7))
ax1 = ax.twinx()

ax.errorbar(lam*10**6, Bp, yerr = yerrorp, fmt = 'b-', elinewidth = 0.7, capsize = 2, label = 'Planet, T = 1000 K')
plt.grid(color = 'k', alpha = 0.5, linestyle = 'dotted', linewidth = 0.6)
ax1.errorbar(lam*10**6, Bs, yerr = yerrors, fmt = 'm-', elinewidth = 0.7, capsize = 2, label = 'Star, T = 5778 K')
ax.axvline(lambp, color = 'r', ls = '--', lw = 0.9, label = '$\lambda_p = {:.3f}$'.format(lambp)+' $\mu m$')
ax1.axvline(lambs, color = 'g', ls = '--', lw = 0.9, label = '$\lambda_p = {:.3f}$'.format(lambs)+' $\mu m$')
ax.set_xlabel(r'Wavelength, $\lambda$ ($\mu m$)')
ax.set_ylabel(r'$B_\lambda$ (T) of Planet ($~Jm^{-2}s^{-1}Hz^{-1}Sr^{-1}$)')
ax1.set_ylabel(r'$B_\lambda$ (T) of Star ($~Jm^{-2}s^{-1}Hz^{-1}Sr^{-1}$)')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.07), ncol=3, fancybox=True, shadow=True)
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=True)
plt.savefig('bb_star_planet.pdf')
plt.show()

fig, ax2 = plt.subplots(figsize = (10, 7))
lam = np.linspace(0.3e-6, 3e-6, 100)
lambp = 2.898
lambs = 2.898/5.778
plt.errorbar(lam*10**6, ratio, yerr = yerrorr, fmt = 'k-', elinewidth = 0.7, capsize = 2, label = r'$\frac{F_p}{F_*}=\frac{B_\lambda (T_p)}{B_\lambda (T_*)}\left(\frac{R_p}{R_*}\right)^{2}$')
plt.axvline(lambp, color = 'k', ls = 'dashdot', lw = 0.9, label = r'Planet $\lambda_p = {:.3f}$'.format(lambp)+' $\mu m$')
plt.axvline(lambs, color = 'k', ls = 'dashed', lw = 0.9, label = r'Star $\lambda_p = {:.3f}$'.format(lambs)+' $\mu m$')
plt.grid(color = 'k', alpha = 0.5, linestyle = 'dotted', linewidth = 0.6)
plt.xlabel(r'Wavelength, $\lambda$ ($\mu m$)')
plt.ylabel(r'Flux Density Ratio, $\frac{F_p}{F_*}$')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12), ncol=3, fancybox=True, shadow=True)
plt.savefig('bb_star_planet_ratio.pdf')
plt.show()


fig, ax3 = plt.subplots(figsize = (10, 7))
aj = 778.57e6
Rj = 71492
A = 0.3

r = 0.3*(Rj/aj)**2
fratio = [r]*len(lam)

plt.plot(lam*10**6, fratio, 'ko-', lw = 0.7, markersize = 2, label = r'$\frac{F_p}{F_*}=A\left(\frac{R_p}{a}\right)^{2}$; A = 0.3')
plt.grid(color = 'k', alpha = 0.5, linestyle = 'dotted', linewidth = 0.6)
plt.text(1, 2.65*10**-9, 'For Jupiter & Sun Like System')
plt.xlabel(r'Wavelength, $\lambda$ ($\mu m$)')
plt.ylabel(r'Flux Density Ratio, $\frac{F_p}{F_*}$')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.8), ncol=3, fancybox=True, shadow=True)
plt.savefig('bb_star_planet_ratio_albedo.pdf')
plt.show()
