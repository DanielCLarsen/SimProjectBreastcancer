import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import heapq
import math

#Task 1

P = np.matrix([[0.9915,0.005,0.0025,0,0.001],
               [0,0.986,0.005,0.004,0.005],
               [0,0,0.992,0.003,0.005],
               [0,0,0,0.991,0.009],
               [0,0,0,0,1]])
n=len(P)
#1 timestep = 1 month; sim 1000 women; start state 1;
cdf=np.zeros((n,n+1))
for i in range(0,n):
    for j in range(1,n+1):
        cdf[i,j] = cdf[i,j-1]+P[i,j-1]

t=0
X=[0]

while X[-1]!=4:
    U=np.random.uniform(0,1)
    for j in range(1,n+1):
        if cdf[X[t],j-1]<U and U<=cdf[X[t],j]:
            X.append(j-1)
    t+=1
#Until death; hist of lifetime dist; 



#Cancer eventually reappear locally?
#Verify with analytical; Use p_t=p_0(P**t)

