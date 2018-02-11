# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:53:38 2018

@author: k
"""

board = [[2,5,1,6,1,4,1],
         [6,1,1,2,2,9,3],
         [7,2,3,2,1,3,1],
         [1,1,3,1,7,1,2],
         [4,1,2,3,4,1,2],
         [3,3,1,2,3,4,1],
         [1,5,2,9,4,7,100]]

def jump(x,y):
    if (x>=len(board) or y>=len(board[0]) ):
        return False
    if (x == (len(board)-1) and y == (len(board[0]) -1)): #board[len(board)-1][(len(board[0])-1)] ==도착지점
        return True
    jumpSize = board[x][y]
    return jump(x+jumpSize,y) or jump(x,y+jumpSize)

jump(0,0)