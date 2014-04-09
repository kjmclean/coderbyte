# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 12:55:43 2014

@author: mcLean
"""

##move everything one place ahead in alphabet
##vowels become uppercase



def LetterChanges(str):
    query = str
    build = ''
    vowels = 'aeiou'
    for char in query:
        if char.isalpha() == True:
            spam = chr(ord(char) + 1)
            if vowels.find(spam) > -1:
                spam = spam.upper()
            build = build + spam
        else:
            build = build + char
    return build

