####################################
#                                  #
#   Code by:                       #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   April 28, 2021                 #
#                                  #
####################################


import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats


shape, scale = 2.0, 2.0
s = np.random.gamma(shape, scale, 100000)


meansample = []
numofsample = [10, 100, 1000, 10000, 100000, 1000000]
samplesize = 100

for i in numofsample:
    eachmeansample = []
    for j in range(0,i):
        rc = random.choices(s, k = samplesize)
        eachmeansample.append(sum(rc)/len(rc))
    meansample.append(eachmeansample)



cols = 2
rows = 3
fig, ax = plt.subplots(rows, cols, figsize = (20, 15))
n = 0
for i in range(0, rows):
    for j in range(0, cols):
        ax[i,j].hist(meansample[n], 200, density = True, color = 'b')
        ax[i,j].set_title(label = "number of sample :" + str(numofsample[n]), size = 8)
        ax[i,j].tick_params(axis = 'both', which = 'major', labelsize = 6)
        ax[i,j].tick_params(axis = 'both', which = 'minor', labelsize = 6)
        ax[i,j].set_xlabel('Range Interval', fontsize = 5)
        ax[i,j].set_ylabel('Probability', fontsize = 5)
        n += 1
plt.subplots_adjust(hspace = 0.6, wspace = 0.4)  
plt.savefig('Central_Theorem1.pdf')      
plt.show()


