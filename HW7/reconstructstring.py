import sys
import operator
import re #regex
from eulerianpath import eulerianPath


def listToStr(list):
	liststring = re.sub('[\[\],\']+', '', str(list))
	liststring = liststring.replace(' ', ',')
	return liststring


with open(sys.argv[1]) as file:

	kmerlen = int(file.readline().strip())
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

	#sortedgraph = sorted(graph.items(), key=lambda x: x[0])

	output = open('graph.txt', 'w')

	for t in graph.keys():
		#print(t[0], ' -> ',  listToStr(t[1]))
		output.write(t + ' -> ' + listToStr(graph[t]) + '\n')

	output.close()

	with open('graph.txt') as outputgraph:
		setup = []
		for line in outputgraph :
			setup.append(line.strip().split(' -> '))

		graph = {}
		for item in setup:
			graph[item[0]] = item[1].split(',')

	# Get the Eulerian path.
	path = eulerianPath(graph)

	lines = [path[0]]
	for i in xrange(1, len(path)):
		lines.append(path[i][kmerlen-2])

	print lines

	with open('output.txt', 'w') as output_data:
		output_data.write(''.join(x for x in lines))
