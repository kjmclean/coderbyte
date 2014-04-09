# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 10:33:49 2014

@author: mcLean
"""

def LongestWord(sen): 
    L = sen.split()
    L2 = []
    for str in L:
        for i in str:
            if i.isalpha() == False:
                str = str.translate(None, i)
        L2 = L2 + [str] 
    x = ''
    for i in L2:
        if len(i) > len(x):
            x = i
    return x
 