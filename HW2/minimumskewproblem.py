'''
Find a position in a genome minimizing the skew.
Given: A DNA string Genome
Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|)

Example

Given input
CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG

Output
53 97
'''


import sys

with open(sys.argv[1]) as file:
	sequence = next(file).strip()

	#print(' '.join([sequence])) #testing

	count = 0
	mincount = 0

	#list of the positions with the minimum skew
	minpos = []

	for i in range(0, len(sequence)):

		if count == mincount:
			minpos.append(i)
		if count < mincount:
			mincount = count
			minpos = [i]

		if sequence[i] == 'G':
			count += 1
		if sequence[i] == 'C':
			count -= 1

	print(' '.join(str(x) for x in minpos))