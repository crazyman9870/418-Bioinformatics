'''
Find All Approximate Occurrences of a Pattern in a String

Given: Strings Pattern and Text along with an integer d.
Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

Given: 
ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
3
Return:
6 7 26 27 78
'''

import sys

with open(sys.argv[1]) as file:
	pattern = next(file).strip()
	sequence = next(file).strip()
	mismatches = int(next(file).strip())

	kmers = []


	for i in range(0, len(sequence) - len(pattern) + 1) :
		kmer = sequence[ i : i + len(pattern)]
		kmers.append(kmer)


	answers = []

	for index, kmer in enumerate(kmers):
		mistakes = 0
		for c in range(len(kmer)):
			if pattern[c] != kmer[c]:
				mistakes += 1
		if mistakes <= mismatches:
			answers.append(str(index))

	print(" ".join(answers))