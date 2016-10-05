'''
Given: A collection of k-mers Patterns.
Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.

Given:
GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG

Return:
AGG -> GGG
CAG -> AGG,AGG
GAG -> AGG
GGA -> GAG
GGG -> GGA,GGG

'''

import sys
import operator
import re #regex

def listToStr(list):
	liststring = re.sub('[\[\],\']+', '', str(list))
	liststring = liststring.replace(' ', ',')
	return liststring


with open(sys.argv[1]) as file:

	kmers = []

	for line in file:
		kmers.append(line.strip())

	graph = {}

	for kmer in kmers:
		prefix = kmer[0:len(kmer)-1]
		suffix = kmer[1:len(kmer)]
		if prefix not in graph:
			graph[prefix] = [suffix]
		else:
			graph[prefix].append(suffix)
			graph[prefix].sort()

	sortedgraph = sorted(graph.items(), key=lambda x: x[0])

	output = open('output.txt', 'w')

	for t in sortedgraph:
		#print(t[0], ' -> ',  listToStr(t[1]))
		output.write(t[0] + ' -> ' + listToStr(t[1]) + '\n')

	output.close()