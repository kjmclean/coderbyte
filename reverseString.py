# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 23:35:51 2014

@author: mcLean
"""
def FirstReverse(str): 
  reverse = ''
  i = 1
  while i <= len(str):
    reverse = reverse + str[-i]
    i = i + 1
  return  reverse
  
#print FirstReverse(raw_input())  





#def reverseString(x):
#    reverse = ''  
#    i = 1
#    while i <= len(x):
#        reverse = reverse + x[-i]
#        i = i + 1
#    print reverse
        
