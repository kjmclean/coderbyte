# -*- coding: utf-8 -*- 

### Using the Python language, have the function ExOh(str) take the str 
### parameter being passed and return the string true if there is an 
### equal number of x's and o's, otherwise return the string false. 
### Only these two letters will be entered in the string, no punctuation 
### or numbers. For example: if str is "xooxxxxooxo" then the output 
### should return false because there are 6 x's and 5 o's.

def ExOh(str): 
	Ex = 0	
	Oh = 0	
	i = 0
	while i < len(str):
		if str[i] == 'x':
			Ex += 1
		else:
			Oh += 1
		i += 1 
	if Ex == Oh:
		return 'true'
	else:
		return 'false'	

# Input = "xooxxo"	Output = "true"
# Input = "x"		Output = "false" 
