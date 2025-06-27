####################################
#                                  #
#   Code by:                       #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   April 10, 2021                 #
#                                  #
####################################


import math 
import random
import numpy as np
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


##############################################################
# This part of the code gives a simple Gaussian Distribution #
##############################################################

mean, sdev = 50, 5
s = np.random.normal(mean, sdev, 10000)
count, bins, ignored = plt.hist(s, 200, density = True, color = 'b', label = 'Random Data')
dist = 1/(sdev * np.sqrt(2 * np.pi)) *np.exp( - (bins - mean)**2 / (2 * sdev**2) )
plt.plot(bins, dist, linewidth = 1, color = 'r', linestyle = 'dashed', label = 'Best Fit Line')
plt.xlabel(r"Income Interval")
plt.ylabel(r"Probability")
plt.title(r"Gaussian Distribution of Income in a Population")
plt.text(57, 0.07, r'$\sigma = 5, \mu = 50$')
plt.text(57, 0.065, r'n = 10000, bins = 200')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.legend()
plt.savefig('Gaussian.pdf')
plt.show()

####################################################################################################
# This part of the code gives comparison of measured and true parameter mu, Slice of 2D histogram, #
# Measured mu's best-fit and uncertainties, pull on mu and it's Gaussian and best-fit.             #
####################################################################################################

Nmeas, Nexp = 10, 10000
sigma = 5.0

mu_best = []
mu_true = []

for i in range(0, 201):
    mu_true_val = float(i)/10.0
    
    for e in range(Nexp):
        mu_best_val = 0.0
        
        for m in range(Nmeas):
            x = random.gauss(mu_true_val, sigma)
            mu_best_val += x
            
                        
        mu_best_val = mu_best_val / float(Nmeas)
        
        mu_best.append(mu_best_val)
        mu_true.append(mu_true_val)
                
'''
LLR = - (np.asarray(x) - np.asarray(mu_best))**2/(2(sigma/np.sqrt(float(Nmeas)))**2)
plt.plot(mu_best, LLR)
plt.show()
'''

### Measured & True Parameters, $\mu$ in 2D Histogram ###
fig, ax = plt.subplots()
hist_mu = plt.hist2d(mu_true, mu_best, bins = 201, norm = LogNorm())   
plt.xlabel(r"$\mu_{true}$")
plt.ylabel(r"$\mu_{measured}$")
plt.title(r"Measured & True Parameters, $\mu$ in 2D Histogram")
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.savefig('2D_Histogram_Mu.pdf')
plt.colorbar(hist_mu[3], ax = ax)
plt.show()

### Slice of the 2D Histogram of $\mu$ Parameter ###
plt.plot(hist_mu[0][:, 100], drawstyle = 'steps', color = 'b', alpha = 0.6)
plt.fill(hist_mu[0][:, 100], 'b', alpha = 0.5)
plt.xlabel(r'$\mu$')
plt.ylabel(r"$P ~ (\mu ~ | ~ \mu_{measured}, \sigma)$")
plt.title(r'Slice of the 2D Histogram of $\mu$ Parameter')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.savefig('Slice_Mu.pdf')
plt.show()

### Histogram of $\mu_{measured}$ with Errors ###
data = np.array(mu_best)
y, binEdges = np.histogram(data, bins = 100)
bincenters = 0.5*(binEdges[1:] + binEdges[:-1])
menStd = np.sqrt(y)
plt.bar(bincenters, y, linewidth = 1, color = 'c', alpha = 0.5, yerr = menStd)
plt.xlabel(r'Range of $\mu$')
plt.ylabel(r"$\mu_{measured}$")
plt.title(r'Histogram of $\mu_{measured}$ with Errors')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.savefig('Measured_Mu_Error.pdf')
plt.show()

### Histogram of $\mu_{measured}$ with Fitting ###
sns.distplot(data, bins = 100, color = 'c', label = r'Best Fitted $\mu_{measured}$')
plt.xlabel(r'Range of $\mu$')
plt.ylabel(r"$\mu_{measured}$") 
plt.title(r'Histogram of $\mu_{measured}$ with Fitting')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.savefig('Measured_Mu_Fit.pdf')
plt.legend()
plt.show()

### Histogram for pull on $\mu$ Parameter: Gaussian Fit ###
pull_mu = (np.asarray(mu_best) - np.asarray(mu_true))/(sigma)
plt.hist(pull_mu, 100, color = 'm', alpha = 0.5,  density = True, label = 'Experimental Pull')
plt.axvline(-0.5, linestyle = 'dashed', color='green', linewidth = 1)
plt.axvline(0.5, linestyle = 'dashed', color='green', linewidth = 1)
#plt.axhline(0.65, linestyle = 'dashed', color='r', linewidth = 1)
width = 0.365 + 0.363
plt.plot((-0.363, 0.365 ), (0.65, 0.65), 'r--', linewidth = 1, label = r'Pull Width = '+'${:.3f}$'.format(width))
plt.text(-0.15, .6, 'FWHM')
mu0, sigma0 = norm.fit(pull_mu)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu0, sigma0)
plt.plot(x, p, 'k--', linewidth = 0.5, label = 'Gaussian Fitted Pull')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dotted', linewidth = 0.7)
plt.xlabel(r'Range of Parameter $\mu$')
plt.ylabel(r"Frequency of Pull on $\mu$")
plt.title(r'Histogram for pull on $\mu$ Parameter')
plt.legend()
plt.savefig('Pull_Mu.pdf')
plt.show()

### Histogram for pull on $\mu$ Parameter: Best-Fit ###
sns.distplot(np.array(pull_mu), bins = 100, color = 'm', label = 'Best Fitted Pull')
plt.axvline(-0.5, linestyle = 'dashed', color='green', linewidth = 1)
plt.axvline(0.5, linestyle = 'dashed', color='green', linewidth = 1)
#plt.axhline(0.65, linestyle = 'dashed', color='r', linewidth = 1)
plt.plot((-0.363, 0.365 ), (0.65, 0.65), 'r--', linewidth = 1, label = r'Pull Width = '+'${:.3f}$'.format(width))
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dotted', linewidth = 0.7)
plt.text(-0.15, .6, 'FWHM')
plt.xlabel(r'Range of Parameter $\mu$')
plt.ylabel(r"Frequency of Pull on $\mu$")
plt.title(r'Histogram for Pull on $\mu$ Parameter')
plt.legend()
plt.savefig('Pull_Mu_BestFit.pdf')
plt.show()




#######################################################################################################
# This part of the code gives comparison of measured and true parameter sigma, Slice of 2D histogram, #
# Measured sigma's best-fit and uncertainties, pull on sigma and it's Gaussian and best-fit.          #
#######################################################################################################

Nmeas, Nexp = 10, 10000
mu = 5

sigma_best = []
sigma_true = []

for j in range(0, 201):
    sigma_true_val = float(j)/10.0
    
    for e in range(Nexp):
        sigma_best_val = 0.0
        x_bar = 0.0
        x_square_bar = 0.0
        
        for m in range(Nmeas):
            x = random.gauss(mu, sigma_true_val)
            x_bar += x
            x_square_bar += x*x
        
        x_bar = x_bar / float(Nmeas - 1)
        x_square_bar = x_square_bar / float(Nmeas - 1)                
        sigma_best_val = math.sqrt(abs(x_square_bar - x_bar*x_bar))
        
        sigma_best.append(sigma_best_val)
        sigma_true.append(sigma_true_val)
        
### Measured & True Parameters, $\sigma$ in 2D Histogram ###  
fig1, ax = plt.subplots()      
hist_sigma = plt.hist2d(sigma_true, sigma_best, bins = 201, norm = LogNorm())   
plt.xlabel(r"$\sigma_{true}$")
plt.ylabel(r"$\sigma_{measured}$")
plt.title(r"Measured & True Parameters, $\sigma$ in 2D Histogram")
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.savefig('2D_Histpgram_Sigma.pdf')
plt.colorbar(hist_sigma[3], ax = ax)
plt.show()

### Slice of the 2D Histogram of $\sigma$ Parameter ###
plt.plot(hist_sigma[0][:, 100], drawstyle = 'steps', color = 'b', alpha = 0.6)
plt.xlabel(r'$\sigma$')
plt.ylabel(r"$P ~ (\sigma ~ | ~ \sigma_{measured}, \mu)$")
plt.title(r'1D Slice of the 2D Histogram of $\sigma$ Parameter')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.savefig('Slice_Sigma.pdf')
plt.show()

### Histogram of $\sigma_{measured}$ with Errors ###
data = np.array(sigma_best)
y, binEdges = np.histogram(data, bins = 100)
bincenters = 0.5*(binEdges[1:] + binEdges[:-1])
menStd = np.sqrt(y)
plt.bar(bincenters, y, linewidth = 1, color = 'c', alpha = 0.5, yerr = menStd)
plt.xlabel(r'Range of $\sigma$')
plt.ylabel(r"$\sigma_{measured}$")
plt.title(r'Histogram of $\sigma_{measured}$ with Errors')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.savefig('Measured_Sigma_Error.pdf')
plt.show()

### Histogram of $\sigma_{measured}$ with Fitting ###
sns.distplot(data, bins = 100, color = 'c', label = r'Best Fitted $\sigma_{measured}$')
plt.xlabel(r'Range of $\sigma$')
plt.ylabel(r"$\sigma_{measured}$") 
plt.title(r'Histogram of $\sigma_{measured}$ with Fitting')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.7)
plt.savefig('Measured_Sigma_Fit.pdf')
plt.legend()
plt.show()

### Histogram for pull on $\sigma$ Parameter: Gaussian-Fit ###
pull_sigma = (np.asarray(sigma_best) - np.asarray(sigma_true))/sigma
plt.hist(pull_sigma, 100, color = 'm', alpha = 0.5, density = True, label = 'Experimental Pull')
plt.axvline(-0.5, linestyle = 'dashed', color='green', linewidth = 1)
plt.axvline(0.5, linestyle = 'dashed', color='green', linewidth = 1)
#plt.axhline(0.5, linestyle = 'dashed', color='r', linewidth = 1)
plt.plot((-0.463, 0.349 ), (0.5, 0.5), 'r--', linewidth = 1, label = r'Pull Width = '+'${:.3f}$'.format(0.349 + 0.463))
plt.text(-0.45, .45, 'FWHM')
mu1, sigma1 = norm.fit(pull_sigma)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu1, sigma1)
plt.plot(x, p, 'k--', linewidth = 0.5, label = 'Gaussian Fitted Pull')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dotted', linewidth = 0.7)
plt.xlabel(r'Range of Parameter $\sigma$')
plt.ylabel(r"Frequency of Pull on $\sigma$")
plt.title(r'Histogram for Pull on $\sigma$ Parameter')
plt.legend()
plt.savefig('Pull_Sigma.pdf')
plt.show()

### Histogram for pull on $\sigma$ Parameter: Best-Fit ###
sns.distplot(np.array(pull_sigma), bins = 100, color = 'm', label = 'Best Fitted Pull')
plt.axvline(-0.5, linestyle = 'dashed', color='green', linewidth = 1)
plt.axvline(0.5, linestyle = 'dashed', color='green', linewidth = 1)
#plt.axhline(0.5, linestyle = 'dashed', color='r', linewidth = 1)
plt.plot((-0.463, 0.349 ), (0.5, 0.5), 'r--', linewidth = 1, label = r'Pull Width = '+'${:.3f}$'.format(0.349 + 0.463))
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dotted', linewidth = 0.7)
plt.text(-0.45, .45, 'FWHM')
plt.xlabel(r'Range of Parameter $\sigma$')
plt.ylabel(r"Frequency of Pull on $\sigma$")
plt.title(r'Histogram for Pull on $\sigma$ Parameter')
plt.legend()
plt.savefig('Pull_Sigma_BestFit.pdf')
plt.show()
