####################################
#                                  #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   March 11, 2021                 #
#                                  #
####################################


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import random


lower_limit = 0
upper_limit = 2*np.pi
n = []



def f(x):
    return np.cos(x)*np.cos(x)
    


for i in range(0,100):
    n.append(int(i+1))
n=np.array(n)


trapezoidal_integral = []
quadrature_integral = [] 
original_integral = []
MC_integral = [] 

for i in n:
    h = (upper_limit - lower_limit)/float(i)
    trap = 0.5*(f(upper_limit) + f(lower_limit))
    for k in range(i):
        trap += f(lower_limit + k*h)
    trapezoidal_integral.append(h*trap)

    quad, difference = integrate.fixed_quad(f, lower_limit, upper_limit , n = i)
    quadrature_integral.append(quad)
    
    
    xrand = random.uniform(lower_limit, upper_limit, i)
    integral = 0
    for j in range(i):
        integral += f(xrand[j])
    MC_integral.append(h*integral)
    
    
    original_integral.append(np.pi)


fig, ax1 = plt.subplots()


ax1.plot(n, quadrature_integral, label = 'Gaussian Quadrature Integral', color = 'blue')
ax1.plot(n, trapezoidal_integral, label = 'Trapezoidal Integral', color = 'green', alpha = 0.75)
ax1.plot(n, MC_integral, linestyle = 'dashed', label = 'Monte Carlo Integration', color = 'red')
ax1.plot(n, original_integral, linestyle = 'dotted', label = r'Original Integral, $\int_{0}^{2\pi}\cos^2(x) \,dx = \pi$', color = 'black')


plt.xlabel('Number of Intervals')
plt.ylabel('True and Estimated Integral Values')
plt.legend()
plt.title('Comparison of Numerical and Monte carlo Integration')   
plt.savefig('MC_Integration.pdf')
plt.show()
