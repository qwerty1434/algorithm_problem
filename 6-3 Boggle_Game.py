# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:45:15 2018

@author: k
"""
import numpy as np

board = np.array([["u","r","l","p","m"],
                  ["x","p","r","e","t"],
                  ["g","i","a","e","t"],
                  ["x","t","n","z","y"],
                  ["x","o","q","r","z"]])

xy = [(-1,1),(0,1),(1,1),
      (-1,0)        ,(1,0)
     ,(-1,-1),(0,-1),(1,-1)]


def boggle(x,y,word): #(x,y)의 시작위치 , 인풋단어 : word
    if x<0 or y<0 or x>=board.shape[0] or y>=board.shape[1]: #시작위치가 판위에 없으면 false
        return False
    if board[x,y]!=word[0]: #첫단어가 틀리면 false
        return False
    if len(word) ==1 : #첫단어가 맞는데 단어가 한글자면 true
        return True
    for (nextX,nextY) in xy: #인접한 8칸 들여다보기
        newx = x+nextX
        newy = y+nextY
        newword = word[1:len(word)]
        if boggle(newx,newy,newword):
            return True

