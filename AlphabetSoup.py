#!/usr/bin/env python

### Have the function AlphabetSoup(str) return the string
### with the letters in alphabetical order. Assume numbers
### and punctuation symbols will not be included in the string.

def AlphabetSoup(str):
    return ''.join(sorted(list(str)))
 
#print AlphabetSoup(raw_input()) 

## test cases: "coderbyte" =>"bcdeeorty"
##              "hooplah"  => "ahhloop"

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
