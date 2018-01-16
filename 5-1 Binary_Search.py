# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:45:36 2018

@author: k
"""

def binary_search(arr, x):
    arr.sort() #오름차순 정렬
    start = 0
    end = len(arr)-1
    while start < end:
        mid = (start+end)// 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid +1
        else:
            end = mid -1
    return None

binary_search(k,3)   
