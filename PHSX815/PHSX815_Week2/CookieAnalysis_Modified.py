#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
from time import time
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()
    t1 = time()
    times = Sorter.QuickSort(times)
    times_avg = Sorter.QuickSort(times_avg)
    t2 = time()
    print(t2-t1)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
    
    weight1 = np.ones_like(times_avg)/len(times_avg)
    weight2 = np.ones_like(times)/len(times)

    title1 = str(Nmeas) + " measurements/experiment with rate " + str(rate) + " cookies/day"
    fig, ax= plt.subplots()
    ax.hist(times_avg, 100, weights = weight1, density=True, alpha = 0.4,  facecolor='r')
    ax.set_yscale('log')
    plt.xlabel("Average time between missing cookies [days]")
    plt.ylabel("Probability")
    plt.title(title1)
    plt.grid(False)
    quant_5, quant_25, quant_50, quant_75, quant_95 = np.quantile(times_avg, 0.05), np.quantile(times_avg, 0.25), np.quantile(times_avg, 0.5), np.quantile(times_avg, 0.75), np.quantile(times_avg, 0.95)
    quants = [[quant_5, 0.6, 0.16], [quant_25, 0.8, 0.26], [quant_50, 1, 0.36],  [quant_75, 0.8, 0.46], [quant_95, 0.6, 0.66]]
    for i in quants:
        ax.axvline(i[0], alpha = i[1], ymax = i[2], linestyle = ":")

    ax.text(quant_5-.1, 0.05, "5th", size = 8, alpha = 0.8)
    ax.text(quant_25-.13, 0.1, "25th", size = 10, alpha = 0.85)
    ax.text(quant_50-.13, 0.15, "50th", size = 11, alpha = 1)
    ax.text(quant_75-.13, 0.2, "75th", size = 10, alpha = 0.85)
    ax.text(quant_95-.25, 0.4, "95th Percentile", size = 8)

    plt.show()

    title2 = "Rate of " + str(rate) + " cookies/day"
    fig1, ax1 = plt.subplots()
    ax1.hist(times, 100, weights = weight2,  density=True, alpha = 0.65, facecolor='m')
    ax1.set_yscale('log')
    plt.xlabel("Time between missing cookies [days]")
    plt.ylabel("Probability")
    plt.title(title2)
    plt.grid(True)
    plt.show()
