# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:08:15 2018

@author: k
"""

import numpy as np
cache = np.full((100,100),-1,dtype=int)


board = [[2,5,1,6,1,4,1],
         [6,1,1,2,2,9,3],
         [7,2,3,2,1,3,1],
         [1,1,3,1,7,1,2],
         [4,1,2,3,4,1,2],
         [3,3,1,2,3,4,1],
         [1,5,2,9,4,7,100]]

def jump(x,y):
    if (x>=len(board) or y>=len(board[0]) ):
        return 0 #없다
    if (x == (len(board)-1) and (y == (len(board[0]) -1))): 
        return 1 #있다
    ret = cache[x][y]
    if ret != -1 :
        return ret
    jumpSize = board[x][y]
    ret= jump(x+jumpSize,y) or jump(x,y+jumpSize)
    print(x,y,ret)
    return ret


