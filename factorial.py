# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 23:00:16 2014

@author: mcLean
"""

def factorial(int):
    i = 1
    answer = 1
    while i <= int:
        answer = answer*i
        i += 1
        print answer
    return answer
    