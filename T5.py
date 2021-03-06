import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import heapq
import math

#Task 5

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
'''
for cCalc in range(0,10):
    print("cCalc: ",cCalc)
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
    varList[cCalc] = np.var(meanList)
    covariance = np.cov(deathFracList,meanList)      
    cList[cCalc] = covariance[0,1]/varList[cCalc]
        

cMean = np.mean(cList) #0.0026699819530815235
'''

#Now we calculate all the other values for another data set than c has been calculated on.
#Lets calculate Z

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

cMean = 0.0026699819530815235
Z = [0]*100
for i in range(0,len(Z)):
    Z[i] = deathFracList[i] + cMean*(meanList[i]-E_T)

varDeathFrac = np.var(deathFracList) #0.00103
varZ = np.var(Z) #0.00254
varRed=(1-varZ/varDeathFrac)*100 # in percentage
#variance using control variate is smaller
# 95% confidence intervals
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t._ppf((1+confidence)/2., n-1)
    return m-h, m, m+h

X_CI=mean_confidence_interval(deathFracList)
Z_CI=mean_confidence_interval(Z)


