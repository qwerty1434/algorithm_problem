# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:00:58 2018

@author: k
"""
def recursive_function_sum(x):
    if x == 1 :
        return 1
    else :
        return x + recursive_function_sum(x-1)
    
