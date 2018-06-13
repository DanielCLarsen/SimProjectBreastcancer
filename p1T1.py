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
#1 timestep = 1 month; sim 1000 women; start state 1;
cdf=np.zeros((len(P),len(P)+1))
for i in range(0,len(P)):
    for j in range(1,len(P)+1):
        cdf[i,j] = cdf[i,j-1]+P[i,j-1]


'''
cdf[0]=0
for i in range(1,7):
    cdf[i]=cdf[i-1]+pdf[i-1]

xCrude = [0]*outcomes
for i in range(0, outcomes):
    for j in range(0,6):
        if cdf[j]<U[i] and cdf[j+1] >= U[i]:
            xCrude[i]=j+1
'''


#Until death; hist of lifetime dist; cancer eventually reappear locally?
#Verify with analytical; Use p_t=p_0(P**t)

