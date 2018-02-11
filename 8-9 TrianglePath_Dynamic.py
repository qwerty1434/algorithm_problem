# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:18:57 2018

@author: k
"""

import numpy as np
cache2 = np.full((100,100),-1,dtype=int)
triangle = [[6,0,0,0,0],
            [1,2,0,0,0],
            [3,7,4,0,0],
            [9,4,1,7,0],
            [2,7,5,9,4]]

def path2(x,y):
    if x==(len(triangle)-1):
        return triangle[x][y]
    ret = cache2[x][y]
    if ret !=-1:
        return ret
    ret = max(path2(x+1,y),path2(x+1,y+1))+triangle[x][y]
    return ret

path2(0,0)
