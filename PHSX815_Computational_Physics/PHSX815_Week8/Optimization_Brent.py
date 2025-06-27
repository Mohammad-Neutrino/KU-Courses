###############################################################################
#                                                                             #
#  Original Code taken from:                                                  #
#  https://scipy-lectures.org/advanced/mathematical_optimization/#id39        #
#                                                                             #
#  Modified By:                                                               #
#  Mohammad Ful Hossain Seikh                                                 #
#  @University of Kansas                                                      #
#  March 28, 2021                                                             #
#                                                                             #
###############################################################################

"""
Illustration of 1D optimization (Minimization): Brent's method
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x = np.linspace(-3, 3, 500)

# A Quadratic plus Gaussian Function
def quadgauss(x):
    return 2.0*(x**2) + 2.0*x + 2.0 + 5.0*np.exp(-x**2)


all_x = list()
all_y = list()
for iter in range(8):
    result = optimize.minimize_scalar(quadgauss, bracket = (-5, 2.9, 4.5), method = "Brent",
             options = {"maxiter": iter}, tol = np.finfo(1.0).eps)

    this_x = result.x
    all_x.append(this_x)
    all_y.append(quadgauss(this_x))
    if iter < 5:
       plt.text(this_x - .05*np.sign(this_x) - .05,
                quadgauss(this_x) + 1.2*(.3 - iter % 2), iter + 1, size = 8, color = 'black')
    
plt.plot(x, quadgauss(x), linewidth = 1, color = 'b', label = r'f(x) = $2(x^2 + x + 1) + 5e^{-x^2}$')
plt.ylabel(r'f(x) = $2(x^2 + x + 1) + 5e^{-x^2}$')
plt.xlabel('x')
plt.title("Minimization of f(x) using Brent's Method")    
plt.plot(all_x[:10], all_y[:10], 'k.', markersize = 5, color = 'r', label = 'Iteration Points')
plt.plot(all_x[-1], all_y[-1], 'rx', markersize = 8, color = 'g', label = 'Minimum Point')
plt.grid(color='c', alpha = 0.7, linestyle='dotted', linewidth = 0.5)
plt.legend()
plt.savefig('Optimization_Brent.pdf')

    
fig, ax = plt.subplots()
ax.semilogy(np.abs(all_y - all_y[-1]), linewidth = 1, color = 'red')
plt.title("Error in Each Iteration: Brent's Method")
plt.ylabel('Error on f(x) in Log Scale')
plt.xlabel('Iteration')
plt.grid(color='b', alpha = 0.5, linestyle='dashed', linewidth = 0.7)
plt.savefig('Optimization_Brent_Error.pdf')

plt.show()

