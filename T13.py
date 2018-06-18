from __future__ import division
import numpy as np
import scipy.stats as stats
import scipy.linalg as linAlg
import matplotlib.pyplot as plt
import heapq
import math

# import data: T12output.spydata

def Q_pdf(Q):
    Q_pdf = np.zeros((n-1,n))
    Q_cdf=np.zeros((n-1,n+1))
    for i in range(0,n-1):
        for j in range(0,n):
            if j!=i:
                Q_pdf[i,j] = -Q[i,j]/Q[i,i]
                Q_cdf[i,j] = Q_cdf[i,j-1]+Q_pdf[i,j-1]
    return Q_pdf

# Initial guess of Q
Q_0=[ [ [],[],[],[],[] ], [ [],[],[],[],[] ], [ [],[],[],[],[] ], [ [],[],[],[],[] ]]
women=1000
n=5

for i in range(women):
    count=1
    for j in range(len(Y[i])-1):
        if Y[i][j]==Y[i][j+1]:
            count+=1
        else:
            Q_0[Y[i][j]][Y[i][j+1]].append(1/(48*count))
            count=1

Q_k=np.zeros(shape=(n-1,n))

for i in range(n-1):
    for j in range(i+1,n):
        Q_k[i,j]=np.mean(Q_0[i][j])
        if math.isnan(Q_k[i,j]):
            Q_k[i,j]=0
        Q_k[i,i]-=Q_k[i,j]
        
        

'''
states = [0,1,2,3,4]
X=[[0] for i in range(women)]
for i in range(women):
    X_temp=[X[i][-1]]
    clock = 0
    temp_clock=0
    count=1
    while X[i][-1]!=4:
        temp_clock += np.random.exponential(1/(-Q_k[X_temp[-1],X_temp[-1]]))
        X_temp.append(np.random.choice(states,p=np.squeeze(Q_pdf[X_temp[-1],:])))
        if temp_clock >= 48*count or X_temp[-1]==4:
            if X_temp[-1]==Y[i][count]:
                X[i]=X[i]+X_temp[1:]
                count+=1
                clock+=temp_clock
            X_temp=[X[i][-1]]
            temp_clock=clock

N=np.zeros((n,n)) # easy to increment using index
S=[0]*n # need to record clock times

for i in range(women):
    for j in range(1,len(X[i])):
        N[X[i][j-1],X[i][j]]]+=1
'''


    
                
                