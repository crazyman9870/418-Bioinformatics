import sys
from compiler.ast import flatten

# Read the input data.
with open(sys.argv[1]) as file:
	kmers = [line.strip() for line in file.readlines()]

# Construct a dictionary of edges.
edges = {}
for kmer in kmers:
	if kmer[:-1] in edges:
		edges[kmer[:-1]].append(kmer[1:])
	else:
		edges[kmer[:-1]] = [kmer[1:]]

# Determine the balanced and unbalanced edges.
balanced, unbalanced = [], []
outVals = reduce(lambda a,b: a+b, edges.values())
for node in set(outVals+edges.keys()):
	out_value = outVals.count(node)
	if node in edges:
		in_value = len(edges[node])
	else:
		in_value = 0

	if in_value == out_value == 1:
		balanced.append(node)
	else:
		unbalanced.append(node)

# Generate the contigs.
get_contigs = lambda s, c: flatten([c+e[-1] if e not in balanced else get_contigs(e,c+e[-1]) for e in edges[s]])
contigs = sorted(flatten([get_contigs(start,start) for start in set(unbalanced) & set(edges.keys())]))

# Print and save the answer.
print '\n'.join(contigs)
with open('outputcontigs.txt', 'w') as outputData:
	outputData.write('\n'.join(contigs))