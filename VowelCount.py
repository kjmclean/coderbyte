### Using the Python language, have the function VowelCount(str)
### take the str string parameter being passed and return the 
### number of vowels the string contains (ie. "All cows eat grass"
### would return 5). Do not count y as a vowel for this challenge. 

def VowelCount(str):
	vowels = 'aeiouAEIOU'
	count = 0	
	for letter in str:
		if vowels.find(letter) >= 0:
			count += 1
	return count


# print VowelCount(raw_input()) 

# Input = "hello" Output = 2
# Input = "coderbyte" Output = 3 
