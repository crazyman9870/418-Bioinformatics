'''
Given: An integer k and a string Text.
Return: Compositionk(Text) (the k-mers can be provided in any order).

Given:
5
CAATCCAAC

Return:
AATCC
ATCCA
CAATC
CCAAC
TCCAA
'''

import sys

with open(sys.argv[1]) as file:

	k = int(next(file).strip())
	seq = next(file).strip()

	kmers = []
	for i in range(len(seq) - k + 1):
		kmer = kmers.append(seq[i:(i+k)])

	kmers.sort()

	print('\n'.join(str(x) for x in kmers))