'''
Finds the most frequent substrings in a given string based on a specific length
Given: A string and a substring length
Return: A list of all most frequent substrings of that legnth (unsorted, can be more than one)

Example

Given input
ACGTTGCATGTCGCATGATGCATGAGAGCT
4

Output
CATG GCAT
'''

import sys

with open(sys.argv[1]) as file:
	seq = next(file).strip() # file.next().strip() Python 2
	kmer_len = int(next(file).strip())

	counts = {}
	for i in range(0, len(seq)):
		kmer = seq[i : i + kmer_len]
		if kmer not in counts:
			counts[kmer] = 1
		else:
			counts[kmer] += 1

	max_count = 0
	max_kmers = []
	for kmer, count in counts.items(): # counts.itermitems() Python 2
		if count > max_count:
			max_count = count
			max_kmers.clear()
			max_kmers.append(kmer)
		elif count == max_count:
			max_kmers.append(kmer)

	print(" ".join(max_kmers)) #print variable Python 2