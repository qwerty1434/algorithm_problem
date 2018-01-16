# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:45:14 2018

@author: k
"""

def prime(x):
    d = 2
    result=[]
    count=0
    while d<=x:
        if x%d ==0:
            result.append(d)
            count+=1
            print(count)
            x = x/d
        else:
            count=0
            d = d+1
    return result


prime(48)
