# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 15:51:21 2014

@author: mcLean
"""

## Using the Python language, have the function TimeConvert(num) take 
## the num parameter being passed and return the number of hours and 
## minutes the parameter converts to (ie. if num = 63 then the output 
## should be 1:3). Separate the number of hours and minutes with a colon. 

## Input = 126 Output = "2:6"
## Input = 45 Output = "0:45" 

def TimeConvert(num):
    x = int(num)
    h = x/60
    min = x%60
    L = [str(h), str(min)]
    print ':'.join(L)
    
