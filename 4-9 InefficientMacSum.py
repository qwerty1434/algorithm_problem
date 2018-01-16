# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:47:16 2018

@author: k
"""

def MaxSum(arr):
    hab=[]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
                hab.append(sum(arr[i:j+1]))
    return max(hab)

