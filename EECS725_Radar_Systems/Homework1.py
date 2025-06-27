import numpy as np
import matplotlib.pyplot as plt 


#-------------------------------------------------------
# Range vs aircraft position x
#-------------------------------------------------------

x = np.linspace(-2000, 2000, 2000) # x-positions of flight track
t_loc = np.asarray([0, -2000, 0]) # target location
# flight locations; x, y = 0, z = 1000
R = []
for i in range(len(x)):
    R.append(np.sqrt((t_loc[0] - x[i])**2 + (t_loc[1] - 0)**2 + (t_loc[2] - 1000)**2))
print('Range R', R, len(R))

plt.plot(x, R, c = 'r') 
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)   
plt.ylabel('Range, R (m)')
plt.xlabel('Aircraft position, x (m)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Fall2023/RangeVsx.png', dpi = 400)
plt.show()


#-------------------------------------------------------
# Angle between v and R vectors vs aircraft position x
#-------------------------------------------------------

gamma = np.rad2deg(np.arccos(x/R))
print('Angle b/w range vector and velocity vector', gamma, len(gamma))

plt.plot(x, 180 - gamma, c = 'b') 
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)   
plt.ylabel(r'Angle between $\vec{R}$ and $\vec{v}$, $\gamma$ ($^\circ$)')
plt.xlabel('Aircraft position, x (m)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Fall2023/GammaVsx.png', dpi = 400)
plt.show()

#-------------------------------------------------------
# Gain vs aircraft position x
#-------------------------------------------------------

c = 3e8 # speed of light in m/s
f = 1e9 # frequency of radar in Hz (or 1/s)
lamb = c/f # wavelength in m
print('wavelength', lamb)

h = 0.1 # antenna aperture height in m
l = 0.5 # antenna aperture length in m

beta_xz = lamb/h
beta_yz = lamb/l
print('betas', beta_xz, beta_yz)

G_0 = (4*np.pi)/(beta_xz*beta_yz)
G_0_dB = 10*np.log10(G_0)
print('gains', G_0, G_0_dB)

r, theta, phi = [], [], []
for i in range(len(x)):   
    r.append(np.sqrt(x[i]**2 + 2000**2 + 1000**2))
    theta.append(np.arccos(1000/np.sqrt(x[i]**2 + 2000**2 + 1000**2)))

    if x[i]<0:
        phi.append(np.arctan(2000/x[i]) + np.pi/2)
    if x[i]>0:
        phi.append(np.arctan(2000/x[i]) - np.pi/2)    

plt.plot(x, r, c = 'r') 
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)   
plt.ylabel(r'r (m)')
plt.xlabel('Aircraft position, x (m)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Fall2023/r.png', dpi = 400)
plt.show()

plt.plot(x, np.asarray(np.rad2deg(theta)), c = 'b', label = r'$\theta$') 
plt.plot(x, 135 - np.asarray(np.rad2deg(theta)), c = 'b', ls = 'dashed', label = r'$135^\circ - \theta$') 
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)   
plt.ylabel(r' $\theta$ ($^\circ$)')
plt.xlabel('Aircraft position, x (m)')
plt.legend()
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Fall2023/theta.png', dpi = 400)
plt.show()

plt.plot(x, np.abs(np.asarray(np.rad2deg(phi))), c = 'g') 
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)   
plt.ylabel(r' $\phi$ ($^\circ$)')
plt.xlabel('Aircraft position, x (m)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Fall2023/phi.png', dpi = 400)
plt.show()
    
sin_theta = 2.773*(- np.asarray(theta) + 3*np.pi/4)/beta_xz
sin_phi = 2.773*np.asarray(phi)/beta_yz

Gain = G_0*((np.sin(sin_theta)/sin_theta)**2)*((np.sin(sin_phi)/sin_phi)**2)

plt.plot(x, 10*np.log10(Gain), c = 'm')
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)   
plt.ylabel(r'Gain, G (dB)')
plt.xlabel('Aircraft position, x (m)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Fall2023/GainVsx.png', dpi = 400)
plt.show()


#-------------------------------------------------------
#  P_r/P_t vs aircraft position x
#-------------------------------------------------------

Pr_Pt = ((lamb**2)*(Gain**2))/(((4*np.pi)**3)*(np.asarray(R)**4))

plt.plot(x, 10*np.log10(Pr_Pt), c = 'c')
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)   
plt.ylabel(r'$P_r/P_t$ (dB)')
plt.xlabel('Aircraft position, x (m)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Fall2023/PrPtVsx.png', dpi = 400)
plt.show()

#-------------------------------------------------------
#  P_r/P_t vs aircraft position x
#-------------------------------------------------------
v = 90 # aircraft velocity in m/s
f_D = -(2/lamb)*v*np.cos(np.deg2rad(gamma))

plt.plot(x, f_D, c = 'orange')
plt.grid(ls = 'dashed', c = 'k', alpha = 0.2, lw = 0.75)   
plt.ylabel(r'Doppler frequency shift, $f_D$ (Hz)')
plt.xlabel('Aircraft position, x (m)')
plt.savefig('/Users/m725s436/Desktop/KU/Coursework/EECS725_Fall2023/fDVsx.png', dpi = 400)
plt.show()