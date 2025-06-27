####################################
#                                  #
#   Code by:                       #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   March 20, 2021                 #
#                                  #
####################################


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import math



emission_number = 100000
mu, sigma, n = 2.0, 0.5, 1000
def normal(x, mu, sigma):
    return (2.0*np.pi*sigma**2.0)**-0.5 * np.exp(-0.5 * (x-mu)**2 / sigma**2.0)

emission_constant1 = np.random.normal(10.0, 1.5, 1000)
rate1 = np.random.choice(emission_constant1)
dist1 = random.poisson(rate1, emission_number)
np.savetxt("dist1.txt", dist1, fmt = '%u')


emission_constant2 = np.random.normal(20.0, 5.0, 1000)
rate2 = np.random.choice(emission_constant2)
dist2 = random.poisson(rate2, emission_number)
np.savetxt("dist2.txt", dist2, fmt = '%u')


file1 = open("dist1.txt", "r")
hypothesis1 = []
for i in file1:
    hypothesis1.append(int(i))
hypothesis1.sort()
#hypothesis1 = np.array(hypothesis1)


file2 = open("dist2.txt", "r")
hypothesis2 = []
for j in file2:
    hypothesis2.append(int(j))  
hypothesis2.sort()      
hypothesis2 = np.array(hypothesis2)



alpha = 0.05
critical_value = hypothesis1[min(int((1 - alpha)*len(hypothesis1)), len(hypothesis1)-1)]
remaining = np.where( hypothesis2 > critical_value)[0][0]
beta = remaining/len(hypothesis2)



k = 0
Liklihood1, Liklihood2 = 0, 0
H1_Liklihood = []
H2_Liklihood = []


for k in range(0, len(hypothesis1)):

    Liklihood1 = (np.exp( - rate1))*(rate1**hypothesis1[k])/np.math.factorial(hypothesis1[k])
    H1_Liklihood.append(Liklihood1)
    
    Liklihood2 = (np.exp( - rate2))*(rate2**hypothesis1[k])/np.math.factorial(hypothesis1[k])
    H2_Liklihood.append(Liklihood2)

hypothesis1.sort()



fig,ax=plt.subplots()

plt.plot([], [], ' ', label = r'$\alpha = {:.3f}$'.format(alpha))
plt.plot([], [], ' ', label = r'$\beta = {:.3f}$'.format(beta))
plt.axvline(critical_value, linestyle = 'dashed', color='green', label = r'$\lambda_{c} = $' + '${:.3f}$'.format(critical_value))
ax.plot(hypothesis1, H1_Liklihood, label = r'$L(H_1):$ $\mu_1 = 10.0$, $\sigma_1 = 1.5$, $\lambda_1 = {:.5f}$'.format(rate1), color = 'black', linestyle = 'dotted')
ax.plot(hypothesis1, H2_Liklihood, label = r'$L(H_2):$ $\mu_2 = 20.0$, $\sigma_2 = 5.0$, $\lambda_2 = {:.5f}$'.format(rate2), color = 'black', linestyle = 'dashed')
plt.legend(loc = 0)

ax.fill_between(hypothesis1, 0, H1_Liklihood, alpha=0.5, color = 'r')
ax.fill_between(hypothesis1, 0, H2_Liklihood, alpha=0.5, color = 'b')

plt.title("Hypothesis 1 & Hypothesis 2 Liklihoods")
plt.xlabel(r"Parameter, $\lambda$")
plt.ylabel("Likelihoods of Two Hypotheses")
#ax.set_yscale('log')
plt.grid(False)
plt.savefig('Likelihoods2.pdf')
plt.show()
