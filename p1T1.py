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
#Until death; hist of lifetime dist; cancer eventually reappear locally?
#Verify with analytical; Use p_t=p_0(P**t)