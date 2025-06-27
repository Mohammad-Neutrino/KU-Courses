import numpy as np
import matplotlib.pyplot as plt



# Given values and constants
t = np.linspace(0, 1.3e-6, 1000) # radar time of operation in s
c = 3e8 # light speed m/s
H = 3e3 # altitude in m
tau = 1e-9 # pulse duration in s
sigma0 = 0.1 
wavelength = 0.1 # in m
phi = np.linspace(0, 0, 1000)
G0 = 10**(16/10) # antenna gain unitless
b_theta, b_phi = np.deg2rad(25), np.deg2rad(25)


# Area vs time
R_L = H + (c*(t + tau)/2)
R_T = H + (c*t/2)
x_L = np.sqrt(R_L**2 - H**2)
x_T = np.sqrt(R_T**2 - H**2)

A = np.pi*(x_L**2 - x_T**2)

plt.plot(t*1e6, A, c = 'b')
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75) 
plt.xlabel(r'Time, t ($\mu s$)')
plt.ylabel(r'Illuminated Ground Area, A(t) ($m^2$)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Radar_Systems_Fall2023/HW3_Area.png', dpi = 400)
plt.show()

# Theta vs time
x_theta = (x_T + x_L)/2
theta = np.arctan2(x_theta, H)

plt.plot(t*1e6, theta*180/np.pi, c = 'r')
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75) 
plt.xlabel(r'Time, t ($\mu s$)')
plt.ylabel(r'Mid Incidence Angle, $\theta(t)$ ($^\circ$)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Radar_Systems_Fall2023/HW3_Theta.png', dpi = 400)
plt.show()

# P_r/P_t vs time
R = np.sqrt(x_theta**2 + H**2)
G = G0*np.exp(-2.773*((theta/b_theta)**2 + (phi/b_phi)**2))
sigma_theta = sigma0*(np.cos(theta))**9
Pr_Pt = ((wavelength**2)*(G**2)*sigma_theta*A)/(((4*np.pi)**3)*(R**4))

plt.plot(t*1e6, 10*np.log10(Pr_Pt), c = 'g')
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)
plt.xlabel(r'Time, t ($\mu s$)')
plt.ylabel(r'$P_r/P_t$ ($dB$)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Radar_Systems_Fall2023/HW3_PrPt.png', dpi = 400)
plt.show()


# Contribution from componensts
a = 10*np.log10(sigma_theta)
b = 10*np.log10(G**2)
c = 10*np.log10(A)
d = 10*np.log10(R**(-4))
e = np.asarray([10*np.log10(wavelength**2/((4*np.pi)**3))]*len(t))

plt.plot(t*1e6, a, label = r'$a = \sigma^o$')
plt.plot(t*1e6, b, label = r'$b = G^2$')
plt.plot(t*1e6, c, label = r'$c = A$')
plt.plot(t*1e6, d, label = r'$d = R^{-4}$')
plt.plot(t*1e6, e, label = r'$e = \lambda^2/(4\pi)^3$')
plt.plot(t*1e6, a + b + c + d + e, c = 'k', ls = 'dashed',  label = r'$a + b + c + d + e$')
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)
plt.legend(loc = 'upper center', ncol = 3, bbox_to_anchor = (0.5, 1.15))
plt.xlabel(r'Time, t ($\mu s$)')
plt.ylabel(r'Contributions from Components, ($dB$)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Radar_Systems_Fall2023/HW3_Contributions.png', dpi = 400)
plt.show()

print(r'dynamic range', max(10*np.log10(Pr_Pt)) - min(10*np.log10(Pr_Pt)))
print(r'dynamic range due to $\sigma^o$', max(a) - min(a))
print(r'dynamic range due to $G^2$', max(b) - min(b))
print(r'dynamic range due to Area', max(c) - min(c))
print(r'dynamic range due to $R^{-4}$', max(d) - min(d))

print('does it pass the sanity check? ', max(10*np.log10(Pr_Pt)) - min(10*np.log10(Pr_Pt)) == max(a + b  + c + d + e) - min(a + b  + c + d + e))