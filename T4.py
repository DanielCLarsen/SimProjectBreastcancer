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

women=1000
survival_times=[0]*women
count=-1
while count<women-1:
    t=0
    X=[0]
    for i in range(0,12):
        U=np.random.uniform(0,1)
        for j in range(1,n+1):
            if cdf[X[t],j-1]<U and U<=cdf[X[t],j]: #Crude check
                X.append(j-1)
        t+=1
    if X[12]!=0 and X[12]!=4:
        count+=1
        while X[-1]!=4:
            U=np.random.uniform(0,1)
            for j in range(1,n+1):
                if cdf[X[t],j-1]<U and U<=cdf[X[t],j]: #Crude check
                    X.append(j-1)
            t+=1
        survival_times[count]=(len(X)-1)
    
#Until death; hist of lifetime dist; 
plt.figure(1)
plt.hist(survival_times,cumulative = False,normed=False)
plt.xlabel("Survival_time")
plt.ylabel("#Women")
plt.title("Survival time distribution for 1000 women")
exp_lifetime=np.mean(survival_times)