import random
import numpy as np
import matplotlib.pyplot as plt


line = []
for i in range(1000):
    line.append(random.gauss(0, 1))
line = np.asarray(line)
np.savetxt("gaussian_random.txt",line)


file = np.loadtxt("gaussian_random.txt")
plt.hist(file,bins=50, color = "r")
plt.title("Random Number Histogram: Gaussian Distribution")
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.legend("d", loc = 0)
plt.show()
