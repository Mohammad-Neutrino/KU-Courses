import random
import numpy as np
import matplotlib.pyplot as plt


line = []
for i in range(1000):
    line.append(random.uniform(0, 1))
line = np.asarray(line)
np.savetxt("uniform_random.txt",line)

file = np.loadtxt("uniform_random.txt")
plt.hist(file, bins=50, color = "b")
plt.title("Random Number Histogram: Uniform Distribution")
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.show()
