from __future__ import division
import numpy as np
import scipy.stats as stats
import scipy.linalg as linAlg
import matplotlib.pyplot as plt
import heapq
import math
    
Q2 = np.matrix([[-0.00475, 0.0025, 0.00125 ,0,0.001],
               [0.0, -0.007, 0.0 ,0.002, 0.005],
               [0.0, 0.0, -0.008, 0.003, 0.005],
               [0.0, 0.0, 0.0, -0.009, 0.009],
               [0.0, 0.0, 0.0, 0.0, 0.0]])

n = len(Q2)
P2 = np.zeros((n-1,n))    
for i in range(0,n-1):
    for j in range(0,n):
        if j!=i:
            P2[i,j] = -Q2[i,j]/Q2[i,i]

cdf2=np.zeros((n-1,n+1))
for i in range(0,n-1):
    for j in range(1,n+1):
        cdf2[i,j] = cdf2[i,j-1]+P2[i,j-1]                  

women = 1000
Y = [[0]*1 for n in range(women)]

for i in range(0,women):
    X=[0]
    clock = 0
    while X[-1]!=4:
        clock += np.random.exponential(1/(-Q2[X[-1],X[-1]]))
        U=np.random.uniform(0,1)
        for j in range(1,n+1):
            if cdf2[X[-1],j-1]<U and U<=cdf2[X[-1],j]: #Crude check
                X.append(j-1)
                break
        if clock >= 48:
            Y[i].append(j-1)
            clock-=48

for i in range(0,women):
    if Y[i][-1]!=4:
        Y[i].append(4)