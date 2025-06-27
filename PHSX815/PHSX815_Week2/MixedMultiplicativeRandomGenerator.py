# Code by: Mohammad Ful Hossain Seikh
# @ University of Kansas February 12, 2021


import random
import numpy as np
import matplotlib.pyplot as plt

# function returns random numbers (between 0 and 1) according to mixed multiplicative congruential
# generator of the form random = (a*seed + c) % m where a, m, c are big prime numbers


def seedMultiplicative(initVal):
    global random
    random = initVal

def MultiplicativeCongruential():
    a = 1317
    c = 3917
    m = 713
    global random
    random = (a*random + c) % m
    return random/m 

seedMultiplicative(55555)

line = []
for i in range(1000):
    line.append(MultiplicativeCongruential())
line = np.asarray(line)
np.savetxt("MixedMultiplicativeRandomNumbers.txt",line)


file = np.loadtxt("MixedMultiplicativeRandomNumbers.txt")
plt.hist(file,bins=50, color = "b")
plt.title("Mixed Multiplicative Congruential Generator")
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.legend("d", loc = 0)
plt.savefig("MixedMultiplicativeRandomGenerator.pdf")
plt.show()
