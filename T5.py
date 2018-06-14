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

T=350
p_0 = np.array([1,0,0,0,0])
p_t=p_0
for tt in range(1,T+1):
    p_t = p_t*P
deathFracTheory = p_t[0,4] 

E_T = 262.3716153127931

deathFracList = [0]*100
meanList = [0]*100
women=200
varList = [0]*10
cList = [0]*10
for cCalc in range(0,10):
    print("cCalc: ",cCalc)
    for ite in range(0,100):
        survival_times=[0]*women
        count=-1
        for j in range(0,women):
            t=0
            X=[0]
            while X[-1]!=4:
                U=np.random.uniform(0,1)
                for j in range(1,n+1):
                    if cdf[X[t],j-1]<U and U<=cdf[X[t],j]: #Crude check
                        X.append(j-1)
                t+=1
            survival_times[j]=(len(X)-1)
            if len(X)<=351:
                count+=1
        #Fraction:
        deathFraction = count/women
        deathFracList[ite] = deathFraction
        #Mean surv:
        meanList[ite] = np.mean(survival_times)
        varList[cCalc] = np.var(meanList)
        covariance = np.cov(deathFracList,meanList)      
        cList[cCalc] = covariance[0,1]/varList[cCalc]
        

cMean = np.mean(cList) #0.002683885232107717

#Now we calculate all the other values for another data set than c has been calculated on.
#Lets calculate Z
for ite in range(0,100):
    survival_times=[0]*women
    count=-1
    for j in range(0,women):
        t=0
        X=[0]
        while X[-1]!=4:
            U=np.random.uniform(0,1)
            for j in range(1,n+1):
                if cdf[X[t],j-1]<U and U<=cdf[X[t],j]: #Crude check
                    X.append(j-1)
            t+=1
        survival_times[count]=(len(X)-1)
        if len(X)<=351:
            count+=1
    #Fraction:
    deathFraction = count/women
    deathFracList[ite] = deathFraction
    #Mean surv:
    meanList[ite] = np.mean(survival_times)

Z = [0]*100
for i in range(0,len(Z)):
    Z[i] = deathFracList[i] + cMean*(meanList[i]-E_T)
    
varDeathFrac = np.var(deathFracList) #0.0008009275000000006
varZ = np.var(Z) #0.0017878243652676975
#variance of variate is higher than crude... doesnt make sense.



