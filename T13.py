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
'''
Q_k=np.zeros(shape=(n-1,n))

for i in range(0,n-1):
    temp=np.random.uniform(0,1,size=n-(i+1))
    Q_k[i,(i+1):n]=temp/sum(temp)
    Q_k[i]=-
'''
# perfect guess for testing
n=5
Q_k = np.matrix([[-0.00475, 0.0025, 0.00125 ,0,0.001],
               [0.0, -0.007, 0.0 ,0.002, 0.005],
               [0.0, 0.0, -0.008, 0.003, 0.005],
               [0.0, 0.0, 0.0, -0.009, 0.009],
               [0.0, 0.0, 0.0, 0.0, 0.0]])

Q_pdf = Q_pdf(Q_k)
women=1000
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


    
                
                