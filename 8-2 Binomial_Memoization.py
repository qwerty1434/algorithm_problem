# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:50:04 2018

@author: k
"""
import numpy as np
cache = np.full((30,30),-1,dtype=int)
def bino2(n,r):
    if(r==0 or n==r):
        return 1
    if cache[n][r] !=-1:
        return cache[n][r]
    cache[n][r] = bino2(n-1,r-1)+bino2(n-1,r)
    return cache[n][r]

bino2(10,3)
