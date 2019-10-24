from math import log2
from cmath import exp, pi
from random import random
import numpy as np

#normal slow dft
def dft(X):
    N = len(X)
    temp  = [0]*N
    for i in range(N):
        for k in range(N):
            temp[i] += X[k] * exp(-2j*pi*i*k/N)

    result = np.asarray(temp)
    return result

#cooley tukey for calculating dft(O(nlogn)) 
def cooley_tukey(X):
    N = len(X)
    if N<=1:
        return X
    even = cooley_tukey(X[0::2])
    odd = cooley_tukey(X[1::2])

    temp = [i for i in range(N)]
    for k in range(N//2):
        temp[k] = even[k] + exp(-2.0j*pi*k/N)*odd[k]
        temp[k+N//2] = even[k] - exp(-2.0j*pi*k/N)*odd[k]
    result = np.asarray(temp)
    return result

#X = [1, 4, 3, 2, 2, 3, 4, 1]
#X = []
#for i in range(10):
    #X.append(random())

#Y = cooley_tukey(X)
#print(Y)
#T = dft(X)
#print(T)

