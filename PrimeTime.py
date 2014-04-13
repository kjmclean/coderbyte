# -*- coding: utf-8 -*- 

### Using the Python language, have the function PrimeTime(num) take the
###  num parameter being passed and return the string true if the parameter 
### is a prime number, otherwise return the string false. The range will be 
### between 1 and 2^16. 


def PrimeTime(num): 
	i = 2 
	while i < num:
		if num%i == 0:
			return 'false'
		else:
			i += 1
	return 'true' 



#print PrimeTime(raw_input())  


# Input = 19 	Output = true
# Input = 110 	Output = false

