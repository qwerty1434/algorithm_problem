# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 09:57:45 2018

@author: k
"""
import collections

x=["a","a","k","a","k","k","k",1,1,1,1,1]


def mode(x):
    box = collections.OrderedDict()
    MajorityCount = 0

    for i in range(0, len(x)):
        count = 0
        box[x[i]] = count
        v = x[i]
        for j in range(0,len(x)):
            if x[j] == v:
                count = count+1
                box[x[i]] = count
                if count>MajorityCount:
                    MajorityCount = count
                    Majority = v
    return Majority 


mode(x)

