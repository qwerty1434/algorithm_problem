# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:23:10 2018

@author: k
"""

def match(w,s):
    pos = 0
    if '?' in w:
        for i in range(len(s)):
            if i<len(s) and i<len(w) and(w[i] =='?' or w[i] == s[i]) and len(w)==len(s):
                return True
            else:
                return False
    else:
        while (pos<len(s) and pos< len(w)) and(w[pos] == '?' or w[pos] == s[pos]): #아직 끝까지 가지 않았고 '?'를 만나거나 1:1대응으로 값이 같다면 ok
            pos += 1
        if pos == len(w) :
            pos == len(s)
            return pos
        if(w[pos] == '*'):
            for skip in range(len(s)-pos):
                if (match(w[pos+1],s[pos+skip])): #s[pos+skip]은 *다음에 나오는 문자 값
                    return True
        return False    


first=['he?p','help','heap','helpp']
second=['*p*','help','papa','hello']
third=['*bb*','babbbc']
match(first[0],first[1])
match(first[0],first[2])
match(first[0],first[3]) 
match(second[0],second[1])
match(second[0],second[2])
match(second[0],second[3])
match(third[0],third[1])



