####################################
#                                  #
#   Code by:                       #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   May 03, 2021                   #
#                                  #
####################################

import numpy as np
import random
import matplotlib.pyplot as plt

def my_ran(rate):

    """
    sample random numbers between 0 and 1
    the transformation x = -1/rate ln(1 - z) gives us z = 1 - exp(-rate*x)
    a random number that obeys the probability distribution
    p(x)dx = rate e**(-rate x) dx just like radioactive decay one
    
    """
    z = random.random()
    return -np.log(1 - z)/rate


N0 = 1000
nuclei_life = []
t_half = 19.3009 # half life of C-10 nuclei
rate = np.log(2)/t_half

for n in range(N0):
    nuclei_life.append(my_ran(rate))

nuclei_life = np.sort(np.array(nuclei_life))
n_half_lives = 10
times = np.linspace(0.0, n_half_lives*t_half, 100)

N_decayed = []
N_undecayed = []

for t in times:
    try: q = np.argwhere(nuclei_life <= t)[-1][0]
    except: q = 0
    N_decayed.append(q)
N_undecayed = N0 - np.array(N_decayed)

residue_daughter = abs(np.array(N_decayed) - np.array(N0 - N0*np.exp(-times*rate)))
residue_parent = abs(np.array(N_undecayed) - np.array(N0*np.exp(-times*rate)))



#################################################################
# Theoretical and Simulated Decay: Formation of Daughter Nuclei #
#################################################################

plt.scatter(times, np.array(N_decayed), s = 5, marker = "x", color = 'b', label = "Simulated Decay")
plt.plot(times, N0 - N0*np.exp(-times*rate), ls = ":", color = "k", label = r"Theoretical Decay: $N_0[1-e^{-\lambda t}]$")
plt.grid(color = 'c', alpha = 0.7, linestyle = 'dotted', linewidth = 0.5)
plt.xlabel(r"$t_{1/2}$ (sec)")
plt.ylabel(r"Number of $^{10}B$ Nuclei")
plt.title('Decay of Carbon-10 Nuclei : Daughter')
plt.xlim(0, n_half_lives*t_half)
plt.ylim(0,)
plt.savefig("Formation_Daughter_Nuclei.pdf")
plt.legend()
plt.show()

###########################################################
# Theoretical and Simulated Decay: Decay of Parent Nuclei #
###########################################################

plt.scatter(times, np.array(N_undecayed), s = 5, marker = "x", color = 'r',  label = "Simulated Decay")
plt.plot(times, N0*np.exp(-times*rate), ls = ":", color = "k", label = r"Theoretical Decay: $N_0 e^{-\lambda t}$")
plt.grid(color = 'c', alpha = 0.7, linestyle = 'dotted', linewidth = 0.5)
plt.xlabel(r"$t_{1/2}$ (sec)")
plt.ylabel(r"Number of $^{10}C$ Nuclei")
plt.title('Decay of Carbon-10 Nuclei : Parent')
plt.xlim(0, n_half_lives*t_half)
plt.ylim(0,)
plt.savefig("Deacy_Parent_Nuclei.pdf")
plt.legend()
plt.show()

######################################
# Parent-daughter Nuclei (Log scale) #
######################################

fig, ax = plt.subplots()
plt.plot(times, N0 - N0*np.exp(-times*rate), ls = ":", color = "b", label = r"Daughter Nuclei: $N_0[1-e^{-\lambda t}]$")
plt.plot(times, N0*np.exp(-times*rate), ls = ":", color = "r", label = r"Parent Nuclei: $N_0 e^{-\lambda t}$")
plt.grid(color = 'c', alpha = 0.7, linestyle = 'dotted', linewidth = 0.5)
ax.set_yscale('log')
plt.xlabel(r"$t_{1/2}$ (sec)")
plt.ylabel("Number of Nuclei")
plt.title('Decay of Carbon-10 Nuclei')
plt.savefig("Parent_daughter_Nuclei.pdf")
plt.legend()
plt.show()

####################################
# Number Uncertainty in C-10 Decay #
####################################
mean = np.mean(residue_daughter)
stdev = np.std(residue_daughter)
plt.plot([], [], ' ', label = r'Mean = {:.3f}'.format(mean))
plt.plot([], [], ' ', label = r'St. Deviation = {:.3f}'.format(stdev))
plt.plot(times, residue_daughter, color = "b", ls = ':', label = r"Error in Daughter Nuclei")
plt.plot(times, residue_parent, color = "r", ls = '--', linewidth = '0.7', label = r"Error in Parent Nuclei")
plt.xlabel(r"$t_{1/2}$ (sec)")
plt.ylabel("Number of Nuclei, |Theoretical - Simulated|")
plt.title('Number Uncertainty in Decay of Carbon-10 Nuclei')
plt.grid(color = 'c', alpha = 0.7, linestyle = 'dotted', linewidth = 0.5)
plt.savefig("Number_Uncertainties_C10_Nuclei.pdf")
plt.legend()
plt.show()

