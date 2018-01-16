# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:03:45 2018

@author: k
"""

def linear_search(arr,x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            return i
    return print("not exist")

