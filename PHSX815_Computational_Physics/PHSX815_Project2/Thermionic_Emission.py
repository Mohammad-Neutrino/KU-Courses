####################################
#                                  #
#   Code by:                       #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   March 19, 2021                 #
#                                  #
####################################


import numpy as np
from numpy import random
import matplotlib.pyplot as plt



emission_number = 100000
mu, sigma, n = 10.0, 0.5, 1000
def normal(x, mu, sigma):
    return (2.0*np.pi*sigma**2.0)**-0.5 * np.exp(-0.5 * (x-mu)**2 / sigma**2.0)



emission_constant1 = np.random.normal(10.0, 1.5, 1000)
rate1 = np.random.choice(emission_constant1)
dist1 = random.poisson(rate1, emission_number)
np.savetxt("dist1.txt", dist1, fmt='%u')


emission_constant2 = np.random.normal(20.0, 5.0, 1000)
rate2 = np.random.choice(emission_constant2)
dist2 = random.poisson(rate2, emission_number)
np.savetxt("dist2.txt", dist2, fmt='%u')


fig1, ax1 = plt.subplots()
ax1.hist(emission_constant1, bins = 70, alpha = 0.6, label = r'$\lambda_1:$ $\mu_1 = 2.0$, $\sigma_1 = 0.5$' , color = 'r', density=True)
ax1.hist(emission_constant2, bins = 70, alpha = 0.6, label = r'$\lambda_2:$ $\mu_2 = 4.0$, $\sigma_2 = 1.0$' , color = 'b', density=True)
plt.title('Gaussian Distribution for Thermionic Emission Rate')
plt.ylabel('Probability Densities')
plt.xlabel('Values')
plt.legend(loc = 0)
plt.savefig('Rate_Distribution.pdf')
plt.grid(True)
plt.show()


fig2, ax2 = plt.subplots()
plt.plot([], [], ' ', label= r'Hypothesis$_i \equiv H_i$')
ax2.hist(dist1, bins = int(rate1) + 18, alpha = 0.6, label = r'$H_1$,  $\lambda_1 = {:.5f}$'.format(rate1), color = 'r', density=True)
ax2.hist(dist2, bins = int(rate2) + 18, alpha = 0.6, label = r'$H_2$,  $\lambda_2 = {:.5f}$'.format(rate2), color = 'b', density=True)
plt.title('Poisson Distribution for Thermionic Emission')
plt.ylabel('Probability of Emission')
#ax2.set_yscale('log')
plt.xlabel('Number of Counts in  1 second')
plt.legend(loc = 0)
plt.savefig('Poisson_Distribution.pdf')
plt.grid(True)
plt.show()

