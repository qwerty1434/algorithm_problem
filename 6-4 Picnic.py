# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:34:43 2018

@author: k
"""
import numpy as np
#입출력 예제
n = 4
input = (0,1,1,2,2,3,3,0,0,2,1,3)

n =6
input = (0,1,0,2,1,2,1,3,1,4,2,3,2,4,3,4,3,5,4,5)

#설정
arr = []
for i in range(0,len(input),2):
    arr.append(sorted(input[i:i+2])) #입력을 2개씩 묶고 빠른순 정렬했다


taken = list(np.full((n), False)) #짝이 결정되었는지 여부를 알아내는 T/F 표 



        
#알고리즘
def countPairings(taken):
    firstFree = -1 #0번째 부터 돌기위해 0보다 작은 -1을 처음값으로 설정
    for i in range(n):
        if not taken[i]: #i번째 친구가 짝이 없으면
            firstFree = i #i번재 친구 짝부터 찾아준다
            break;
    if firstFree ==-1: #모든 학생이 짝을 찾았으면
        return 1; #한가지 방법으로 취급 #여기서 return하면 밑에 for문은 실행되지 않는다
    ret = 0 ;
    for pairWith in range(i+1,n): # pairWith는 i보다 크다
        if (not taken[pairWith]) and ([i,pairWith] in arr ): #pairWith가 아직 선택되지 않고 and i랑 pairWith가 짝이면
            taken[firstFree] = True #i 짝찾기 성공
            taken[pairWith] = True #pairWith 짝찾기 성공
            print("===============")
            print(i)
            print(pairWith)
            print(taken)
            print("===============")            
            #밑에 3줄 이해안감
            ret += countPairings(taken) #여기서 한싸이클 끝
            taken[firstFree] = False; #계속 FFFF로 루프를 돌기위해
            taken[pairWith] = False; #계속 FFFF로 루프를 돌기위해
    return ret;        


countPairings(taken)

