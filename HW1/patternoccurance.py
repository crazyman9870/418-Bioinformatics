<<<<<<< HEAD
'''
Finds all occurrences of a pattern in a string
Given: A substring/pattern and a string to search
Return: A list of indicies where that substring begins in the string

Example

Given input
ATAT
GATATATGCATATACTT

Output
1 3 9
'''


import sys

with open(sys.argv[1]) as file:
	substr = next(file).strip()
	sequence = next(file).strip()
	substr_len = len(substr)
	indicies = []

	#print(' '.join([substr, sequence, str(substr_len)])) #testing

	for i in range(0, len(sequence)):
		teststr = sequence[i:(i+substr_len)]
		#print(teststr) #testing
		if teststr == substr:
			indicies.append(i)

	print(' '.join(str(x) for x in indicies))

=======
'''
Finds all occurrences of a pattern in a string
Given: A substring/pattern and a string to search
Return: A list of indicies where that substring begins in the string

Example

Given input
ATAT
GATATATGCATATACTT

Output
1 3 9
'''


import sys

with open(sys.argv[1]) as file:
	substr = next(file).strip()
	sequence = next(file).strip()
	substr_len = len(substr)
	indicies = []

	#print(' '.join([substr, sequence, str(substr_len)])) #testing

	for i in range(0, len(sequence)):
		teststr = sequence[i:(i+substr_len)]
		#print(teststr) #testing
		if teststr == substr:
			indicies.append(i)

	print(' '.join(str(x) for x in indicies))

>>>>>>> origin/master
	