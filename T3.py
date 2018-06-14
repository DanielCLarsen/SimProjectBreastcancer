import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import heapq
import math

def life_time_pdf(t,pi,Ps,p0):
    return float(pi*((Ps)**t)*p0)

#Task 3
n=5
P = np.matrix([[0.9915,0.005,0.0025,0,0.001],
               [0,0.986,0.005,0.004,0.005],
               [0,0,0.992,0.003,0.005],
               [0,0,0,0.991,0.009],
               [0,0,0,0,1]])
pi=np.matrix([[1,0,0,0]])
Ps=P[0:n-1,0:n-1]
p0=P[0:4,4]
I=np.identity(n-1)
one=np.matrix([[1],[1],[1],[1]])

E_T=float(pi*np.linalg.inv(I-Ps)*one)

cdf=np.zeros((n,n+1))
for i in range(0,n):
    for j in range(1,n+1):
        cdf[i,j] = cdf[i,j-1]+P[i,j-1]

women=1000
survival_times=[0]*women
for i in range(0,women):
    t=0
    X=[0]
    while X[-1]!=4:
        U=np.random.uniform(0,1)
        for j in range(1,n+1):
            if cdf[X[t],j-1]<U and U<=cdf[X[t],j]: #Crude check
                X.append(j-1)
        t+=1
    survival_times[i]=(len(X)-1)
mean_emp=np.mean(survival_times)
var_emp=np.var(survival_times)

# t-test of mean
Ttest=(mean_emp-E_T)/np.sqrt(var_emp/women)
p=2*stats.t.cdf(-abs(Ttest),df=women-1)

    
#Until death; hist of lifetime dist; 
plt.figure(1)
surv_ret=plt.hist(survival_times,normed=True)
plt.xlabel("Survival_time")
plt.ylabel("#Women")
plt.title("Survival time distribution for 1000 women")
T=max(survival_times)
time=list(range(0,T))
theory_pdf=[0]*T
for i in range(T):
    theory_pdf[i]=life_time_pdf(i,pi,Ps,p0)

plt.plot(time,theory_pdf)

# chi-squared test of distribution
# The bin partitioning is not integer
# so we use floor to calc expected frequencies
def chi2Test_surv(n,bins,pi,Ps,p0):
    f_obs = [0]*(len(bins)-1)
    f_exp = [0]*(len(bins)-1)
    for i in range(0,len(bins)-1):
        f_obs[i] = n[i]*(bins[i+1]-bins[i])
        for t in range(int(np.floor(bins[i])),int(np.floor(bins[i+1]))):
            f_exp[i]+=float(pi*(Ps**t)*p0)
    chisq, p = stats.chisquare(f_obs,f_exp)
    return chisq, p 

n = surv_ret[0]
bins = surv_ret[1]
chisq_surv, p_surv = chi2Test_surv(n,bins,pi,Ps,p0)