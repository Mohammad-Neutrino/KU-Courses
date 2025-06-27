
####################################
#                                  #
#   Code by:                       #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   April 29, 2021                 #
#                                  #
####################################

import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt



data = pd.DataFrame(np.random.randn(1000, 2), columns = ["Random1", "Random2"])
X = data[["Random1", "Random2"]]
plt.scatter(X["Random1"], X["Random2"], c = 'black', s = 4)
plt.xlabel('Random Numbers 1')
plt.ylabel('Random Numbers 2')


K = 3
Centroids = (X.sample(n = K))
plt.scatter(X["Random1"], X["Random2"], c = 'green', s = 4, alpha = 0.5)
plt.scatter(Centroids["Random1"], Centroids["Random2"], c = 'red', s = 45)
plt.xlabel('Random Numbers 1')
plt.ylabel('Random Numbers 2')
plt.savefig("Centroids.pdf")
plt.show()





diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["Random1"]-row_d["Random1"])**2
            d2=(row_c["Random2"]-row_d["Random2"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos = i+1
        C.append(pos)
    X["Cluster"] = C
    Centroids_new = X.groupby(["Cluster"]).mean()[["Random2", "Random1"]]
    if j == 0:
        diff=1
        j = j+1
    else:
        diff = (Centroids_new['Random2'] - Centroids['Random2']).sum() + (Centroids_new['Random1'] - Centroids['Random1']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["Random2", "Random1"]]
    
    
color = ['blue', 'cyan', 'm']
for k in range(K):
    data = X[X["Cluster"] == k+1]
    plt.scatter(data["Random1"], data["Random2"], c = color[k], s = 5)
plt.scatter(Centroids["Random1"], Centroids["Random2"], c = 'red', s = 45, marker = "*")
plt.title('Data Points and Cluster Centroids')
plt.xlabel('Random Numbers 1')
plt.ylabel('Random Numbers 2')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dotted', linewidth = 0.7)
plt.savefig("KMeans_Cluster_Random.pdf")
plt.show()


