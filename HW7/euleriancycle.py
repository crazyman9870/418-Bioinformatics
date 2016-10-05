'''
Find an Eulerian Cycle in a Graph

Given: An Eulerian directed graph, in the form of an adjacency list.
Return: An Eulerian cycle in this graph.

Given:
0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6

Return:
6->8->7->9->6->5->4->2->1->0->3->2->6
'''
'''
import sys

def EulerianCycle(currentGraph, currentNode):
	edgeCount = len(currentGraph[currentNode])

	if edgeCount > 0:
		nextNode = currentGraph[currentNode][0]
		currentGraph[currentNode].pop(0)

		return(currentNode + '->' + EulerianCycle(currentGraph, nextNode))
	else:
		return currentNode


with open(sys.argv[1]) as file:

	setup = []
	for line in file:
		setup.append(line.strip().split(' -> '))

	graph = {}
	for item in setup:
		graph[item[0]] = item[1].split(',')

	for node in graph:
		answer = EulerianCycle(graph, node)
		break
	print(answer)
	print(len(answer))
'''
import sys

def eulerianCycle(edges):
	'''Generates an Eulerian cycle from the given edges.'''

	for x in edges:
		currentNode = x
		break

	path = [currentNode]

	# Get the initial cycle.
	while True:
		path.append(edges[currentNode][0])

		if len(edges[currentNode]) == 1:
			del edges[currentNode]
		else:
			edges[currentNode] = edges[currentNode][1:]

		if path[-1] in edges:
			currentNode = path[-1]
		else:
			break

	# Continually expand the initial cycle until we're out of edges.
	while len(edges) > 0:
		for i in range(len(path)):
			if path[i] in edges:
				currentNode = path[i]
				cycle = [currentNode]
				while True:
					cycle.append(edges[currentNode][0])

					if len(edges[currentNode]) == 1:
						del edges[currentNode]
					else:
						edges[currentNode] = edges[currentNode][1:]

					if cycle[-1] in edges:
						currentNode = cycle[-1]
					else:
						break

				path = path[:i] + cycle + path[i+1:]
				break
	return path

if __name__ == '__main__':

	# Read the input data.
	with open(sys.argv[1]) as file:

		setup = []
		for line in file:
			setup.append(line.strip().split(' -> '))

		graph = {}
		for item in setup:
			graph[item[0]] = item[1].split(',')
	# Get the Eulerian cycle.
	path = eulerianCycle(graph)

	# Print and save the answer.
	print('->'.join(map(str,path)))
	#print(len(path))
	with open('output2.txt', 'w') as output_data:
		output_data.write('->'.join(map(str,path)))