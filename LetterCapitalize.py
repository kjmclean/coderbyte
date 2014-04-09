# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 17:33:27 2014

@author: mcLean
"""

## Using the Python language, have the function LetterCapitalize(str)
## take the str parameter being passed and capitalize the first letter
## of each word. Words will be separated by only one space.

#Input = "hello world"Output = "Hello World"
#Input = "i ran there"Output = "I Ran There"


def LetterCapitalize(str):
    L = str.split()
    L2 = []
    for word in L:
        word = word[0].upper() + word.lstrip(word[0])
        L2 = L2 + [word]
    x = ' '.join(L2)
    return x