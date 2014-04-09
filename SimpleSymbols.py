# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:03:02 2014

@author: mcLean
"""

## Using the Python language, have the function SimpleSymbols(str) 
## take the str parameter being passed and determine if it is an 
## acceptable sequence by either returning the string true or false. 
## The str parameter will be composed of + and = symbols with several
## letters between them (ie. ++d+===+c++==a) and for the string to be
## true each letter must be surrounded by a + symbol. So the string
## to the left would be false. The string will not be empty and will
## have at least one letter.

#Input = "+d+=3=+s+"Output = "true"
#Input = "f++d+"Output = "false"

def SimpleSymbols(str):
    for char in str:
        #print char
        if char.isalpha() == True:
            if str[0].isalpha() == True:
                print 'False'
                return
            elif str[-1].isalpha() == True:
                print 'False'
                return
            elif str[str.index(char)-1] != '+':
                print 'False'
                return
            elif str[str.index(char)+1] != '+':
                print 'False'
                return
    print 'True'

