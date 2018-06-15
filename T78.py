import numpy as np
import scipy.stats as stats
import scipy.linalg as linAlg
import matplotlib.pyplot as plt
import heapq
import math

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t._ppf((1+confidence)/2., n-1)
    return m-h, m, m+h

def var_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    v= np.var(a)
    v_low=(n-1)*v/stats.chi2.ppf((1+confidence)/2.,n-1)
    v_up=(n-1)*v/stats.chi2.ppf((1-confidence)/2.,n-1)
    return v_low, v, v_up

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
disCount = 0
for i in range(0,women):
    X=[0]
    clock = 0
    isCounted = False
    while X[-1]!=4:
        clock += np.random.exponential(1/(-Q[X[-1],X[-1]]))
        U=np.random.uniform(0,1)
        if isCounted==False and clock<=30.5 and X[-1] == 2 or X[-1] == 3:
            disCount += 1
            isCounted = True
            
        for j in range(1,n+1):
            if cdf[X[-1],j-1]<U and U<=cdf[X[-1],j]: #Crude check
                X.append(j-1)
                break
                
    survTime[i]=clock
    
plt.figure(1)
plt.hist(survTime,cumulative = True,normed=True)
plt.xlabel("Survival_time")
plt.ylabel("#Women")
plt.title("Survival time distribution for 1000 women")

meanCI = mean_confidence_interval(survTime)
varCI = var_confidence_interval(survTime)
stdCI = np.sqrt(varCI)
#Proportion of women cancer reapeared within 30.5 months DISTANTLY.
proportion = disCount/women

#-----------------------------------------------------------------------
#-----------------T8----------------------------------------------------

ms = int(np.ceil(max(survTime)))
Qs=Q[0:4,0:4]
ones = np.matrix([[1],[1],[1],[1]])
p_0 = np.matrix([[1,0,0,0]])
F_theory = [0]*women
F_emp = [0]*women
sortSurv = np.sort(survTime)
for i in range(0,women):
     F_theory[i] = float(1-p_0*linAlg.expm(Qs*sortSurv[i])*ones)
     F_emp[i]=i/women

plt.plot(sortSurv,F_theory)

df = [abs(F_theory_i - F_emp_i) for F_theory_i, F_emp_i in zip(F_theory, F_emp)]

D = max(df)

res = (np.sqrt(women)+0.12+0.11/np.sqrt(women))*D # vs 1.358 at 95%














    