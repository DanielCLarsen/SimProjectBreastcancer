from __future__ import division
import numpy as np
import scipy.stats as stats
import scipy.linalg as linAlg
import matplotlib.pyplot as plt
import heapq
import math

# import data: T12output.spydata

# Initial guess of Q
n=5
Q_k=np.zeros(shape=(n,n))

'''
for i in range(0,n):
    temp=np.random.uniform(0,1,size=n-(i+1))
    Q_k[i,(i+1):n]=temp/sum(temp)
    Q_k[i]=-
'''