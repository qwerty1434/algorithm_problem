# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:08:02 2018

@author: k
"""
#선택정렬
def selection_sort(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i] #앞에가 뒤에보다 크면 둘의 순서를 바꾼다
    return a


"""
입력값: [5,1,2,4,3]
i,j값  정렬되는과정
(0,1) [1,5,2,4,3]
(0,2) [1,5,2,4,3]
(0,3) [1,5,2,4,3]
(0,4) [1,5,2,4,3]
(1,2) [1,2,5,4,3]
(1,3) [1,2,5,4,3]
(1,4) [1,2,5,4,3]
(2,3) [1,2,4,5,3]
(2,4) [1,2,3,5,4]
(3,4) [1,2,3,4,5]
"""
#삽입정렬
def insertion_sort(a):
    for i in range(len(a)):
        key = a[i]
        j = i-1 #점점 작아지면서 찾는다
        while j>=0 and a[j] > key : #삽입하고자 하는 값이 더 크면 그대로 유지
            a[j+1] = a[j]
            j = j-1
        #삽입하는 값이 더이상 크지 않거나 끝까지 다찾아봤으면 삽입
        a[j+1] = key
    return a
