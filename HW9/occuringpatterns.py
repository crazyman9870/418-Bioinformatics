import sys
from suffixarray import constructSuffixArray
from burrowswheelertransform import BWT


def getMultiPatternCount(word, patterns):
	'''Precomputes the necessary information and passes each pattern to multiple pattern matching function.'''
	# Construct the Burrows-Wheeler Transform and Suffix Array.
	bwt = BWT(word)
	suffixArray = constructSuffixArray(word)

	# Create the count dictionary.
	symbols = set(bwt)
	currentCount = {ch:0 for ch in symbols}
	count = {0:{ch:currentCount[ch] for ch in symbols}}
	for i in xrange(len(bwt)):
		currentCount[bwt[i]] += 1
		count[i+1] = {ch:currentCount[ch] for ch in symbols}

	# Get the index of the first occurrence of each character in the sorted Burrows-Wheeler Transformation.
	sortedBWT = sorted(bwt)
	firstOccurrence = {ch:sortedBWT.index(ch) for ch in set(bwt)}

	# Pass the information and patters along to the BWMatching algorithm.
	matches = []
	for pattern in patterns:
		matches += multiPatternMatchBW(bwt, suffixArray, firstOccurrence, count, pattern)
	return matches


def multiPatternMatchBW(bwt, suffixArray, firstOccurrence, count, pattern):
	'''
	Returns the starting index of each occurrence of pattern in the given word using a
	slightly modified version of the Better BW Matching algorithm from Assignment 10D.
	'''
	top, bottom = 0, len(bwt) - 1
	while top <= bottom:
		if pattern != '':
			symbol = pattern[-1]
			pattern = pattern[:-1]
			if symbol in bwt[top:bottom+1]:
				top = firstOccurrence[symbol] + count[top][symbol]
				bottom = firstOccurrence[symbol] + count[bottom+1][symbol] - 1
			else:
				return []
		else:
			return [suffixArray[i] for i in xrange(top, bottom+1)]


def main():
	'''Main call. Reads, runs, and saves problem specific data.'''
	# Read the input data.
	with open(sys.argv[1]) as inputData:
		word = inputData.readline().strip()
		patterns = [line.strip() for line in inputData.readlines()]

	# Get the pattern locations.  Sort for convenience, then map to strings.
	patternLocations = getMultiPatternCount(word, patterns)
	patternLocations = map(str, sorted(patternLocations))

	# Print and save the answer.
	print(' '.join(patternLocations))
	with open('output.txt', 'w') as outputData:
		outputData.write(' '.join(patternLocations))

if __name__ == '__main__':
	main()