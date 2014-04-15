# -*- coding: utf-8 -*- 

### Using the Python language, have the function ArithGeo(arr) take the array of 
### numbers stored in arr and return the string "Arithmetic" if the sequence follows 
### an arithmetic pattern or return "Geometric" if it follows a geometric pattern. 
### If the sequence doesn't follow either pattern return -1. An arithmetic sequence 
### is one where the difference between each of the numbers is consistent, where as 
### in a geometric sequence, each term after the first is multiplied by some constant 
### or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric 
### example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 
### will not be entered, and no array will contain all the same elements.

### Use the Parameter Testing feature in the box below to test your code 
### with different arguments.

def ArithGeo(arr):
	result = ''
	x = 1
	while x < len(arr):
		print 'Loop', x
		if (arr[1]/arr[0]) == arr[x]/arr[x-1]:
			result = 'Geometric'
			print x, arr[x], arr[x-1], result	
			x += 1  	
		elif (arr[1] -arr[0]) == arr[x] - arr[x-1]:
			result = 'Arithmetic'
			x += 1
		else:
			result = -1
			x = len(arr)
	return result
# incorrect when [1, 2, 3, 4, 5, 10, 20]
# incorrect when [-3, -4, -5, -6, -7]
#Divide all numbers by the first number, if modulo = 0, it's geometric
#Subtract 1st from 2nd, and 2nd from 3rd, if it equals the same number,
#it's arithmetic.
#if neither, then it's neither.`

### Input = 5,10,15	Output = "Arithmetic"
### Input = 2,4,16,24	Output = -1
