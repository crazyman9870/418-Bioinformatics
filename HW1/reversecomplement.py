'''
Finds the Reverse Complement of a DNA sequence(string)
Given: A DNA string
Return: A reverse complement DNA string

Example

Given input
AAAACCCGGT

Output
ACCGGGTTTT
'''

import sys

with open(sys.argv[1]) as file:
	seq = next(file).strip() #strips whitespace

	#find the reverse
	revseq = seq[::-1]

	'''
	#testing reverse is correct
	print(' '.join([seq,revseq]))
	'''

	revcomp = ''
	for i in revseq:		
		if i == 'A':
			revcomp += 'T'
		elif i == 'T':
			revcomp += 'A'
		elif i == 'C':
			revcomp += 'G'
		elif i == 'G':
			revcomp += 'C'

	print(''.join(revcomp))