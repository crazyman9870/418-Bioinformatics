import sys

def overlapAlignment(v, w):
	'''Returns the overlap alignment of strings v and w.'''

	# Initialize the arrays.
	S = [[0 for repeatJ in xrange(len(w)+1)] for repeatI in xrange(len(v)+1)]
	backtrack = [[0 for repeatJ in xrange(len(w)+1)] for repeatI in xrange(len(v)+1)]

	# Initialize the max score.
	maxScore = -3*(len(v) + len(w))

	# Fill in the Score and Backtrack arrays.
	for i in xrange(1, len(v)+1):
		for j in xrange(1, len(w)+1):
			# Match score = 1, Mismatch and Indels = -2.
			scores = [S[i-1][j-1] + [-2, 1][v[i-1] == w[j-1]], S[i-1][j] - 2, S[i][j-1] - 2]
			S[i][j] = max(scores)
			backtrack[i][j] = scores.index(S[i][j])

			# Check if we have a new maximum along the last row or column and update accordingly.
			if i == len(v) or j == len(w):
				if S[i][j] > maxScore:
					maxScore = S[i][j]
					maxIndices = (i, j)

	# Initialize i and j as their corresponding index of the maximum score.
	i, j = maxIndices

	# Initialize the aligned strings as the input strings, removing the unused tails.
	vAligned, wAligned = v[:i], w[:j]

	# Quick lambda function to insert indels.
	insertInDel = lambda word, i: word[:i] + '-' + word[i:]

	# Backtrack to the first row or column from the highest score in the last row or column.
	while i*j != 0:
		if backtrack[i][j] == 1:
			i -= 1
			wAligned = insertInDel(wAligned, j)
		elif backtrack[i][j] == 2:
			j -= 1
			vAligned = insertInDel(vAligned, i)
		else:
			i -= 1
			j -= 1

	# Remove the unused head the aligned strings.
	vAligned, wAligned = vAligned[i:], wAligned[j:]

	return str(maxScore), vAligned, wAligned

if __name__ == '__main__':

	# Read the input data.
	with open(sys.argv[1]) as inputData:
		word1, word2 = [line.strip() for line in inputData.readlines()]

	# Get the alignment.
	alignment = overlapAlignment(word1, word2)

	# Print and save the answer.
	print '\n'.join(alignment)
	with open('output.txt', 'w') as outputData:
		outputData.write('\n'.join(alignment))