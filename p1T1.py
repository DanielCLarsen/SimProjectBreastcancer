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
local_count=0
for i in range(0,women):
    local_cancer=False
    t=0
    X=[0]
    while X[-1]!=4:
        U=np.random.uniform(0,1)
        for j in range(1,n+1):
            if cdf[X[t],j-1]<U and U<=cdf[X[t],j]: #Crude check
                X.append(j-1)
                if j-1==1: #If state 2 reached
                    local_cancer=True
        t+=1
    if local_cancer==True:
        local_count+=1
    survival_times[i]=(len(X)-1)
    
#Until death; hist of lifetime dist; 
plt.figure(1)
plt.hist(survival_times,cumulative = True,normed=True)
plt.xlabel("Survival_time")
plt.ylabel("#Women")
plt.title("Survival time distribution for 1000 women")
#Cancer eventually reappear locally?
proportion = local_count/women*100

#Verify with analytical; Use p_t=p_0(P**t)
p_0 = np.array([1,0,0,0,0])

max_t=max(survival_times)
death_prop=[0]*max_t
death_prop[0]=p_0[4]
p_t=p_0
for tt in range(1,max_t):
    p_t = p_t*P
    death_prop[tt]=p_t[0,4]
plt.plot(list(range(0,max_t)),death_prop)