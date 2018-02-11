# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:50:19 2018

@author: k
"""
import numpy as np

N="12345678"

def classify (a,b):
    M = N[a:b]
    if M==M[0]*len(M): #동일한 값이 반복되면
        return 1
    progressive = True
    for i in range(len(M)-1): #등차수열이면
        if (int(M[i+1])-int(M[i])) != (int(M[1])-int(M[0])):
            progressive  = False
    if progressive and (abs(int(M[1])-int(M[0])) == 1): #공차가 1이나 -1이면
        return 2
    alternating = True
    for i in range(len(M)):
        if M[i] != M[i%2]: #홀수번쨰끼리랑 짝수번째끼리가 다르면
            alternating = False
    if alternating :#두 수가 번갈아 나오면 ex)1212
        return 4
    if progressive : #공차가 1,-1이 아닌 등차수열이면
        return 5
    return 10 #아무거도 아니면


cache = np.full(10002,-1)


def memorize(begin):
    if begin == len(N):
        return 0
    ret = cache[begin]
    if ret != -1:
        return ret
    ret = 987654321
    for L in range(3,6): #3~5까지
        if (begin + L) <=len(N):
            ret = min(ret, memorize(begin+L)+classify(begin,begin+L-1))
    return ret

memorize(0)
