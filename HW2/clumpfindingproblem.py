'''
Find patterns forming clumps in a string
Given: A string Genome, and integers k, L, and t.
Return: All distinct k-mers forming (L, t)-clumps in Genome.

Example

Given input
CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
5 75 4

Output
CGACA GAAGA AATGT
'''


import sys

with open(sys.argv[1]) as file:
	sequence = next(file).strip()
	numbers = next(file).strip().split(" ")

	k = int(numbers[0])
	L = int(numbers[1])
	t = int(numbers[2])

	#using a map to avoid duplicates
	kmers = {}

	#Run through the sequence
	for i in range(0, len(sequence) - L + 1):
		#interval is a substring in the seqeunce of size L
		interval = sequence[ i : i + L]

		#Run through the substring
		for j in range(0, len(interval) - k + 1):
			#kmer is a substring in a substring
			kmer = interval[ j : j + k]
			count = interval.count(kmer)

			if count == t:
				kmers[kmer] = 'added to result set'

	print(" ".join(list(kmers.keys())))