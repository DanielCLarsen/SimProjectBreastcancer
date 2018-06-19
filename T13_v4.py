from __future__ import division
import numpy as np
import scipy.stats as stats
import scipy.linalg as linAlg
import matplotlib.pyplot as plt
import heapq
import math

Q2 = np.matrix([[-0.00475, 0.0025, 0.00125 ,0,0.001],
               [0.0, -0.007, 0.0 ,0.002, 0.005],
               [0.0, 0.0, -0.008, 0.003, 0.005],
               [0.0, 0.0, 0.0, -0.009, 0.009],
               [0.0, 0.0, 0.0, 0.0, 0.0]])
n = len(Q2)
P2 = np.zeros((n-1,n))    
for i in range(0,n-1):
    for j in range(0,n):
        if j!=i:
            P2[i,j] = -Q2[i,j]/Q2[i,i]

cdf2=np.zeros((n-1,n+1))
for i in range(0,n-1):
    for j in range(1,n+1):
        cdf2[i,j] = cdf2[i,j-1]+P2[i,j-1]                 

women = 1000
Y = [[0]*1 for n in range(women)]
states=[0,1,2,3,4]
for i in range(0,women):
    X=[0]
    clock = 0
    TimeInState=[0]
    while X[-1]!=4:
        clock += np.random.exponential(1/(-Q2[X[-1],X[-1]]))
        TimeInState.append(clock)
        X.append(np.random.choice(states,p=P2[X[-1],:]))
    count=1
    for j in range(len(X)-1):
        while TimeInState[j]<48*count and 48*count<TimeInState[j+1]:
            Y[i].append(X[j])
            count+=1
    Y[i].append(4)
        
#################################################EX12###########################
def defaultQk(): #Default special treatment Q-matrix
    Q_k=np.matrix([[-0.00475, 0.0025, 0.00125 ,0,0.001],
               [0.0, -0.007, 0.0 ,0.002, 0.005],
               [0.0, 0.0, -0.008, 0.003, 0.005],
               [0.0, 0.0, 0.0, -0.009, 0.009]])
    return Q_k

def Q_pdf(Q): #Finds pdf of Q matrix
    pdf = np.zeros((n-1,n))
    cdf=np.zeros((n-1,n+1))
    for i in range(0,n-1):
        for j in range(0,n):
            if j!=i:
                pdf[i,j] = -Q[i,j]/Q[i,i]
                cdf[i,j] = cdf[i,j-1]+pdf[i,j-1]
    return pdf

women=1000
n=5
Q_0=[ [ [],[],[],[],[] ], [ [],[],[],[],[] ], [ [],[],[],[],[] ], [ [],[],[],[],[] ]]
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


pdf = Q_pdf(Q_k)
states=[0,1,2,3,4]; epsilon=0.001; Q_kp1=np.zeros(shape=(n-1,n)); Norm_inf=1
Inf_norm=1
Q_list = [Q_k]
k=0
N_list = []
S_list = []
while Inf_norm>epsilon:
    Q_k=Q_list[k]
    N=np.zeros((n,n)) # easy to increment using index
    S=[0]*n # need to record clock times
    print("------------------------------")
    print("INF-NORM: ",Inf_norm)
    for w in range(women):    
        for i in range(len(Y[w])-1): #loop Y
            if Y[w][i]==Y[w][i+1]:#Repetitions
                S[Y[w][i]]+=48
            else: #Change in state
                TimeInState = [0]
                X = [Y[w][i]] #Start from current state
                while X[-1]!=Y[w][i+1]: #Run until X is desired state
                    reject = False
                    q=np.sum(Q_k[X[-1],X[-1]+1:Y[w][i+1]+1]) #q transition sum rate
                    if X[-1] == Y[w][i]: #If X is start state
                        temp_time=48
                        while temp_time>=48: #A time lower than 48 is generated
                            temp_time=np.random.exponential(1/q)
                    else:
                        temp_time=np.random.exponential(1/q)# time generated once
                        if temp_time+TimeInState[-1] >=48: #If it is larger than 48 when summed with the previous, reject.
                            reject = True
                    if reject:
                        TimeInState = [0]
                        X = [Y[w][i]]
                    else:    
                        TimeInState.append(TimeInState[-1]+temp_time) #<48 (happen before known state)
                        p = list((pdf[X[-1],X[-1]+1:Y[w][i+1]+1])/np.sum((pdf[X[-1],X[-1]+1:Y[w][i+1]+1]))) #p normalized
                        states = list(range(X[-1]+1,Y[w][i+1]+1)) #Possible outcome states
                        X.append(np.random.choice(states,p=p)) #Get X
                            
                for j in range(0,len(X)-1): #Change N and S
                    N[X[j],X[j+1]] +=1 #Number of jumps incremented
                    S[X[j]] += TimeInState[j] #Time for given state added
                S[Y[w][i+1]]+=48-TimeInState[-1] #remaining time added
    for i in range(n-1):
        for j in range(n):
            Q_kp1[i,j]=N[i,j]/S[i]
        Q_kp1[i,i]=-sum(Q_kp1[i,:])
    Q_list.append(Q_kp1)
    Inf_norm=np.amax(abs(Q_list[k+1]-Q_list[k]))
    k+=1
    S_list.append(S)
    N_list.append(N)
