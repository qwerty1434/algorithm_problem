# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:42:38 2018

@author: k
"""

def bino(n,r):
    if(r==0 or n==r):
        return 1
    print(bino(n-1,r-1))
    return bino(n-1,r-1)+bino(n-1,r)

bino(5,2)
"""
bino(5,2)=bino(4,1)+bino(4,2)
         =bino(3,0)+bino(3,1)+bino(3,1)+bino(3,2)
         =bino(3,0)+2{bino(2,0)+bino(2,1)}+bino(2,1)+bino(2,2)
         =bino(3,0)+2{bino(2,0)+bino(1,0)+bino(1,1)}+bino(1,0)+bino(1,1)+bino(2,2)
         =1+2{1+1+1}+1+1+1
         =10
"""            
