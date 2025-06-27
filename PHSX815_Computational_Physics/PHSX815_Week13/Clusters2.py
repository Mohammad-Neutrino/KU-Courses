

####################################
#                                  #
#   Code by:                       #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   April 29, 2021                 #
#                                  #
####################################


import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
import numpy as np




X, _ = make_blobs(n_samples = 1000, centers  =3, n_features = 2,
                 cluster_std = 0.2,  random_state = 0)

print ("2D data points:\n")
print (X, "\n\n")
    
kmeans = KMeans(n_clusters = 3, random_state = 0).fit(X)


print ("Cluster Centroids:\n")
print(kmeans.cluster_centers_, "\n")
print(kmeans.labels_, "\n")

plt.scatter(X[:, 0], X[:, -1], color = 'cyan', s = 4)    
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'red', marker = '*', s = 5)   
plt.title('Data Points and Cluster Centroids')
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dotted', linewidth = 0.7)
plt.savefig("KMeans_Cluster.pdf")
plt.show()
