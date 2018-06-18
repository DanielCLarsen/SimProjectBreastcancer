from __future__ import division
import numpy as np
import scipy.stats as stats
import scipy.linalg as linAlg
import matplotlib.pyplot as plt
import heapq
import math

# import data: T12output.spydata

def Q_pdf(Q):
    pdf = np.zeros((n-1,n))
    cdf=np.zeros((n-1,n+1))
    for i in range(0,n-1):
        for j in range(0,n):
            if j!=i:
                pdf[i,j] = -Q[i,j]/Q[i,i]
                cdf[i,j] = cdf[i,j-1]+pdf[i,j-1]
    return pdf

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
'''
Q_k=np.zeros(shape=(n-1,n))

for i in range(n-1):
    for j in range(i+1,n):
        Q_k[i,j]=np.mean(Q_0[i][j])
        if math.isnan(Q_k[i,j]):
            Q_k[i,j]=0
        Q_k[i,i]-=Q_k[i,j]
'''
#test with correct Q
Q_k=np.matrix([[-0.00475, 0.0025, 0.00125 ,0,0.001],
               [0.0, -0.007, 0.0 ,0.002, 0.005],
               [0.0, 0.0, -0.008, 0.003, 0.005],
               [0.0, 0.0, 0.0, -0.009, 0.009],
               [0.0, 0.0, 0.0, 0.0, 0.0]])

pdf = Q_pdf(Q_k)
epsilon=0.001
states=[0,1,2,3,4]
N=np.zeros((n,n)) # easy to increment using index
S=[0]*n # need to record clock times

for i in range(women):
    TimeInState=[0]
    count=0
    X_traj=[Y[i][count]]
    while count<(len(Y[i])-1):
        print(count)
        advance=True
        TimeInState.append(TimeInState[-1]+np.random.exponential(1/(-Q_k[X_traj[-1],X_traj[-1]])))
        X_traj.append(np.random.choice(states,p=np.squeeze(pdf[X_traj[-1],:])))
        if TimeInState[-1]>=48 or X_traj[-1]==4:
            nComparisons=max(int(np.floor(TimeInState[-1]/48)),1)
            for j in range(1,nComparisons+1):
                if Y[i][count+j]!=X_traj[-2]:
                    advance=False
                    break
            if count+nComparisons<len(Y[i]) and X_traj[-1]>Y[i][count+nComparisons]:
                advance=False
            if advance==True:
                count+=nComparisons
                for jump in range(len(X_traj)-1):
                    N[X_traj[jump],X_traj[jump+1]]+=1
                    S[X_traj[jump]]+=TimeInState[jump+1]
            X_traj=[Y[i][count]]
            TimeInState=[0]