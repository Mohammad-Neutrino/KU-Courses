####################################
#                                  #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   March 7, 2021                  #
#                                  #
####################################


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


lower_limit = 0
upper_limit = 2*np.pi
n = []


def f(x):
    return np.cos(x)*np.cos(x)
    


for i in range(0,100):
    n.append(int(i+2))
n=np.array(n)


trapezoidal_integral = []
quadrature_integral = [] 
original_integral = [] 
 

for i in n:
    h = (upper_limit - lower_limit)/float(i)
    trap = 0.5*(f(upper_limit) + f(lower_limit))
    for k in range(i):
        trap += f(lower_limit + k*h)
    trapezoidal_integral.append(h*trap)

    quad, difference = integrate.fixed_quad(f, lower_limit, upper_limit , n = i)
    quadrature_integral.append(quad)
    
    original_integral.append(np.pi)



fig, ax1 = plt.subplots()

ax1.plot(n, quadrature_integral, label = 'Gaussian Quadrature Integral', color = 'blue')
ax1.plot(n, trapezoidal_integral, label = 'Trapezoidal Integral', color = 'green', alpha = 0.75)
ax1.plot(n, original_integral, linestyle = 'dotted', label = r'Original Integral, $\int_{0}^{2\pi}\cos^2(x) \,dx = \pi$', color = 'red')

plt.xlabel('Number of Intervals')
plt.ylabel('True and Estimated Integral Values')
plt.legend()
plt.title('Comparison of Trapezoidal Rule and Gaussian Quadrature')   
plt.savefig('Integration.pdf')
plt.show()
