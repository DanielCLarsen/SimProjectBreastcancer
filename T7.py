import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import heapq
import math

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t._ppf((1+confidence)/2., n-1)
    return m-h, m, m+h


Q = np.matrix([[-0.0085,0.005,0.0025,0,0.001],
               [0.0,-0.014,0.005,0.004,0.005],
               [0.0,0.0,-0.008,0.003,0.005],
               [0.0,0.0,0.0,-0.009,0.009],
               [0.0,0.0,0.0,0.0,0.0]])
n = len(Q)
P = np.zeros((n-1,n))    
for i in range(0,n-1):
    for j in range(0,n):
        if j!=i:
            P[i,j] = -Q[i,j]/Q[i,i]

cdf=np.zeros((n-1,n+1))
for i in range(0,n-1):
    for j in range(1,n+1):
        cdf[i,j] = cdf[i,j-1]+P[i,j-1]                    
    
    
    

    
    
women = 1000
survTime = [0]*women
clock = 0
for i in range(0,women):
    t=0
    X=[0]
    clock = 0
    while X[-1]!=4:
        clock += np.random.exponential(-Q[X[t],X[t]])
        U=np.random.uniform(0,1)
        for j in range(1,n+1):
            if cdf[X[t],j-1]<U and U<=cdf[X[t],j]: #Crude check
                X.append(j-1)
        t+=1
    survTime[i]=clock
    

plt.figure(1)
plt.hist(survTime,cumulative = True,normed=True)
plt.xlabel("Survival_time")
plt.ylabel("#Women")
plt.title("Survival time distribution for 1000 women")
#From 1 to death
#histogram
#mean/conf interval/stnd dev with conf int
#Proportion of women cancer reapeared within 30.5 months DISTANTLY.
    
    
'''
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

------

for ite in range(0,100):
        survival_times=[0]*women
        count=0
        for i in range(0,women):
            t=0
            X=[0]
            while X[-1]!=4:
                U=np.random.uniform(0,1)
                for j in range(1,n+1):
                    if cdf[X[t],j-1]<U and U<=cdf[X[t],j]: #Crude check
                        X.append(j-1)
                t+=1
            survival_times[i]=len(X)-1
            if len(X)<=351:
                count+=1
        #Fraction:
        deathFracList[ite] = float(count)/women
        #Mean surv:
        meanList[ite] = np.mean(survival_times)
'''
