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

Q1 = np.matrix([[-0.0085,0.005,0.0025,0,0.001],
               [0.0,-0.014,0.005,0.004,0.005],
               [0.0,0.0,-0.008,0.003,0.005],
               [0.0,0.0,0.0,-0.009,0.009],
               [0.0,0.0,0.0,0.0,0.0]])
    
Q2 = np.matrix([[-0.00475, 0.0025, 0.00125 ,0,0.001],
               [0.0, -0.007, 0.0 ,0.002, 0.005],
               [0.0, 0.0, -0.008, 0.003, 0.005],
               [0.0, 0.0, 0.0, -0.009, 0.009],
               [0.0, 0.0, 0.0, 0.0, 0.0]])
n = len(Q1)
P1 = np.zeros((n-1,n))
P2 = np.zeros((n-1,n))    
for i in range(0,n-1):
    for j in range(0,n):
        if j!=i:
            P1[i,j] = -Q1[i,j]/Q1[i,i]
            P2[i,j] = -Q2[i,j]/Q2[i,i]

cdf1=np.zeros((n-1,n+1))
cdf2=np.zeros((n-1,n+1))
for i in range(0,n-1):
    for j in range(1,n+1):
        cdf1[i,j] = cdf1[i,j-1]+P1[i,j-1]
        cdf2[i,j] = cdf2[i,j-1]+P2[i,j-1]                  

women = 1000
survTime1 = [0]*women
for i in range(0,women):
    X=[0]
    clock = 0
    while X[-1]!=4:
        clock += np.random.exponential(1/(-Q1[X[-1],X[-1]]))
        U=np.random.uniform(0,1)
        for j in range(1,n+1):
            if cdf1[X[-1],j-1]<U and U<=cdf1[X[-1],j]: #Crude check
                X.append(j-1)
                break
    survTime1[i]=clock

survTime2 = [0]*women
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
    survTime2[i]=clock
    
sortSurv1 = np.sort(survTime1)
sortSurv2 = np.sort(survTime2)
S = [0]*women
#S2 = [0]*women
for i in range(0,women):
    D = i/women
    S[i] = (women-D)/women

plt.figure(1)
plt.plot(sortSurv1,S, label='No treatment',color="red")
plt.plot(sortSurv2,S, label='Treatment',color="blue")
plt.legend()
# blue is better.


#####TASK 10###########
#J = np.sort(set().union(list(sortSurv1),list(sortSurv2)))
J = np.sort(np.union1d(sortSurv1,sortSurv2))
nEvents=len(J)
O1 =[0]*nEvents
O2 =[0]*nEvents
O =[0]*nEvents
E =[0]*nEvents
N1 =[0]*nEvents
N2 =[0]*nEvents
N =[0]*nEvents
V =[0]*nEvents
for i in range(1,nEvents):
    if J[i] in sortSurv1:
        O1[i]=O1[i-1]+1
    else:
        O1[i]=O1[i-1]
    if J[i] in sortSurv2:
        O2[i]=O2[i-1]+1
    else:
        O2[i]=O2[i-1]

    O[i]=O1[i]+O2[i]
    N1[i]=women-O1[i]
    N2[i]=women-O2[i]
    N[i]=N1[i]+N2[i]
    E[i]=(O[i]/N[i])*N1[i] 
    V[i]=O[i]*(N1[i]/N[i])*(1-N1[i]/N[i])*(N[i]-O[i])/(N[i]-1)


















    