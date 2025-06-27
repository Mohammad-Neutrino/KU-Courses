import numpy as np
import matplotlib.pyplot as plt

c = 3e8 # speed of light in m/s
f = 1e9 # radar frequency in Hz
l = 5 # antenna dimension in m
tau = 50 # pulse duration in mus
theta = (37/180)*np.pi # mid swath incidence angle in rad
h = 330e3 # altitude in m
R_e = 6378.145e3 # Earth's radius in m
mu = 398600 # standard gravitational parameter in km3/s2 for Earth

beta_az = (c/f)/l # elevation able in rad
print(beta_az*180/np.pi)

gamma = np.arcsin((R_e/(R_e + h))*np.sin(theta)) # look angle in rad
alpha = theta - gamma # core angle in rad
R = ((R_e + h)/np.sin(theta))*np.sin(alpha) # range in m




# for near edge
x_n = alpha*R_e - 25*1e3
print('x_n', x_n/1e3)

alpha_n = x_n/R_e
print('alpha_n', alpha_n, alpha_n*180/np.pi)

R_n = np.sqrt(R_e**2 + (R_e + h)**2 - 2*R_e*(R_e + h)*np.cos(alpha_n))
print('R_n', R_n/1e3)

gamma_n = np.arcsin((R_e/R_n)*np.sin(alpha_n)) 
print('gamma_n', gamma_n, gamma_n*180/np.pi)

theta_n = gamma_n + alpha_n
print('theta_n', theta_n, theta_n*180/np.pi)

T_n = 2*R_n/c
print('T_n', T_n*1e3)


'''
gamma_n = gamma - (beta_el/2) # look angle at near edge in rad
theta_n = np.arcsin(((R_e + h)/R_e)*np.sin(gamma_n)) # incidence angle at near edge in rad
alpha_n = theta_n - gamma_n # core angle at near edge in rad
R_n = ((R_e + h)/np.sin(theta_n))*np.sin(alpha_n) # near edge range in m
x_n = alpha_n*R_e
T_n = 2*R_n/c
'''



# for far edge

x_f = x_n + 50*1e3
print('x_f', x_f/1e3)

alpha_f = x_f/R_e
print('alpha_f', alpha_f, alpha_f*180/np.pi)

R_f = np.sqrt(R_e**2 + (R_e + h)**2 - 2*R_e*(R_e + h)*np.cos(alpha_f))
print('R_f', R_f/1e3)

gamma_f = np.arcsin((R_e/R_f)*np.sin(alpha_f)) 
print('gamma_f', gamma_f, gamma_f*180/np.pi)

theta_f = gamma_f + alpha_f
print('theta_f', theta_f, theta_f*180/np.pi)

T_f = 2*R_f/c
print('T_f', T_f*1e3)


'''
gamma_f = gamma + (beta_el/2) # look angle at far edge in rad
theta_f = np.arcsin(((R_e + h)/R_e)*np.sin(gamma_f)) # incidence angle at far edge in rad
alpha_f = theta_f - gamma_f # core angle at far edge in rad
R_f = ((R_e + h)/np.sin(theta_f))*np.sin(alpha_f) # far edge range in m
x_f = alpha_f*R_e
T_f = 2*R_f/c
'''

# PRFs

PRF_max = 1/(T_f - T_n + 2*tau*1e-6)
print('PRF_max', PRF_max)

v = np.sqrt(mu/(R_e/1e3 + h/1e3))
v_g = v*R_e/(R_e + h)
PRF_min = 2*v*1e3/l
print('PRF_min', PRF_min)


W_gr = (c/2)*(1/np.sin(theta))*((1/PRF_min) - 2*tau*1e-6)
print('swath width', W_gr/1e3)

N_n = PRF_max*(T_n - tau*1e-6)
N_f = PRF_max*(T_f + tau*1e-6) 
print('maximum number of pulse in the air is between', np.ceil(N_n), 'and', np.ceil(N_f))