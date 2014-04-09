# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 13:05:28 2014

@author: mcLean
"""

## Using the Python language, have the function SimpleAdding(num) add up 
## all the numbers from 1 to num. For the test cases, the parameter num 
## will be any number from 1 to 1000.

def SimpleAdding(num):
    count = 0
    sum = 0
    while count <= num:
        sum = sum + count
        count += 1
    return sum
    
    
        