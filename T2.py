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
T=120
n=len(P)
#1 timestep = 1 month; sim 1000 women; start state 1;
cdf=np.zeros((n,n+1))
for i in range(0,n):
    for j in range(1,n+1):
        cdf[i,j] = cdf[i,j-1]+P[i,j-1]

women=1000
state_count=[0]*n

for i in range(0,women):
    t=0
    X=[0]
    while len(X)<=T:
        U=np.random.uniform(0,1)
        for j in range(1,n+1):
            if cdf[X[t],j-1]<U and U<=cdf[X[t],j]: #Crude check
                X.append(j-1)
        t+=1
    state_count[X[T]]+=1

p_t_emp=[i/women for i in state_count]

#Verify with analytical; Use p_t=p_0(P**t)
p_0 = np.array([1,0,0,0,0])
p_t=p_0
for tt in range(1,T+1):
    p_t = p_t*P

test=0
for i in range(0,n):
    test+=((p_t_emp[i]-p_t[0,i])**2)/p_t[0,i]
    

p=1-stats.chi2.cdf(test,df=n-1)

temp = (np.asarray(p_t.T))[:,0]

chi2, p1 = stats.chisquare(p_t_emp,temp)