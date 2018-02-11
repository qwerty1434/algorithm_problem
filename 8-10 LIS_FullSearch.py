# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:38:31 2018

@author: k
"""
A=[3,2,1,7,5,4,6]


def lis(A):
    if len(A)==0:
        return 0
    ret = 0
    B=[]    
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]<A[j]:
                B.append(A[j])
        ret = max(ret,1+lis(B))
        B=[]
    return ret;

lis(A)            
