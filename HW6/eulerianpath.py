import sys

from euleriancycle import eulerianCycle

def eulerianPath(edges):
    '''Returns an Eulerian path from the given edges.'''
    # Determine the unbalanced edges.
    outVals = reduce(lambda a,b: a+b, edges.values())
    for node in set(outVals+edges.keys()):
        outVal = outVals.count(node)
        if node in edges:
            inVal = len(edges[node])
        else:
            inVal = 0

        if inVal < outVal:
            unbalancedFrom = node
        elif outVal < inVal:
            unbalancedTo = node

    # Add an edge connecting the unbalanced edges.
    if unbalancedFrom in edges:
        edges[unbalancedFrom].append(unbalancedTo)
    else:
        edges[unbalancedFrom] = [unbalancedTo]

    # Get the Eulerian Cycle from the edges, including the unbalanced edge.
    cycle = eulerianCycle(edges)

    # Find the location of the unbalanced edge in the eulerian cycle.
    dividePt = filter(lambda i: cycle[i:i+2] == [unbalancedFrom, unbalancedTo], xrange(len(cycle)-1))[0]

    # Remove the unbalanced edge, and shift appropriately, overlapping the head and tail.
    return cycle[dividePt+1:]+cycle[1:dividePt+1]


if __name__ == '__main__':

    # Read the input data.
    with open(sys.argv[1]) as file:

        setup = []
        for line in file:
            setup.append(line.strip().split(' -> '))

        graph = {}
        for item in setup:
            graph[item[0]] = item[1].split(',')

    # Get the Eulerian path.
    path = eulerianPath(graph)

    # Print and save the answer.
    print '->'.join(map(str,path))
    #print(len(path))
    with open('output.txt', 'w') as output_data:
        output_data.write('->'.join(map(str,path)))
