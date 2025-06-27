####################################
#   Original Code by:              #
#   Professor Christopher Rogan    #
#   (in ROOT macros)               #
#                                  #
#   Converted (in Python) by:      #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   March 26, 2021                 #
#                                  #
####################################

import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import random

Nmeas, Nexp = 1, 100000
mu_experiment, sigma = 0, 2

mu_best = []
mu_true = []

for i in range(-100, 101):
    mu_true_val = float(i)/10.0
    
    for e in range(Nexp):
        mu_best_val = 0.0
        
        for m in range(Nmeas):
            x = random.gauss(mu_true_val, sigma)
            mu_best_val += x
                        
        mu_best_val = mu_best_val / float(Nmeas)
        
        mu_best.append(mu_best_val)
        mu_true.append(mu_true_val)


plt.hist2d(mu_true, mu_best, bins = 201, norm = LogNorm())   
plt.xlabel(r"$\mu_{true}$")
plt.ylabel(r"$\mu_{measured}$")
plt.title("Measured & True Parameters in 2D Histogram")
plt.colorbar()
plt.grid(True)
plt.savefig('parameter_mu_1meas_100000exp.pdf')
plt.show()
        
        
