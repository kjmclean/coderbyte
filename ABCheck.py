### Using the Python language, have the function ABCheck(str) take the str 
### parameter being passed and return the string true if the characters a and b 
### are separated by exactly 3 ### places anywhere in the string at least once
### (ie. "lane borrowed" would result in true because there is exactly three 
### characters between a and b). Otherwise return the string false. 

#Input = "after badly" Output = "false"
#Input = "Laura sobs"  Output = "true" 

def ABCheck(spam):
	x = 'false'
	count = 0 
	while count < (len(spam)-4):
		if spam[count] == 'a':
			if spam[count + 4] == 'b': #problem when "+4" is longer than str 
				x = 'true'	
		count += 1
	return x
 
#print ABCheck(raw_input())  
