# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:47:31 2018

@author: k
"""

y=[] 
def moving_average(x,m):
    for i in range(0+m-1,len(x)):
        y.append(np.sum(x[i-m+1:i+1])/m)
