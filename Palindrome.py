# -*- coding: utf-8 -*- 

### Using the Python language, have the function Palindrome(str) take the str 
### parameter being passed and return the string true if the parameter is a 
### palindrome, (the string is the same forward as it is backward) otherwise 
### return the string false. For example: "racecar" is also "racecar" backwards. 
### Punctuation and numbers will not be part of the string. 

def Palindrome(str):
	sparrow = str.replace(' ', '')	
	spam = '' 
	for letter in sparrow:
		spam = letter + spam
	if spam == sparrow:
		return 'true'
	else:
		return 'false'

# Input = "never odd or even"	Output = "true"
# Input = "eye"			Output = "true" 
