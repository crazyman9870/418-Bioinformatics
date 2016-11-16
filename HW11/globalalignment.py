import sys

from scripts import BLOSUM62

def global_alignment(v, w, scoringMatrix, sigma):

	# Initialize the matrices.
	S = [[0 for repeatJ in xrange(len(w)+1)] for repeatI in xrange(len(v)+1)]
	backtrack = [[0 for repeatJ in xrange(len(w)+1)] for repeatI in xrange(len(v)+1)]

	# Initialize the edges with the given penalties.
	for i in xrange(1, len(v)+1):
		S[i][0] = -i*sigma
	for j in xrange(1, len(w)+1):
		S[0][j] = -j*sigma

	# Fill in the Score and Backtrack matrices.
	for i in xrange(1, len(v)+1):
		for j in xrange(1, len(w)+1):
			scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoringMatrix[v[i-1], w[j-1]]]
			S[i][j] = max(scores)
			backtrack[i][j] = scores.index(S[i][j])

	# Quick lambda function to insert indels.
	insertIndel = lambda word, i: word[:i] + '-' + word[i:]

	# Initialize the aligned strings as the input strings.
	vAligned, wAligned = v, w

	# Get the position of the highest scoring cell in the matrix and the high score.
	i, j = len(v), len(w)
	maxScore = str(S[i][j])

	# Backtrack to the edge of the matrix starting at the highest scoring cell.
	while i*j != 0:
		if backtrack[i][j] == 0:
			i -= 1
			wAligned = insertIndel(wAligned, j)
		elif backtrack[i][j] == 1:
			j -= 1
			vAligned = insertIndel(vAligned, i)
		else:
			i -= 1
			j -= 1

	# Prepend the necessary preceeding indels to get to (0,0).
	for repeat in xrange(i):
		wAligned = insertIndel(wAligned, 0)
	for repeat in xrange(j):
		vAligned = insertIndel(vAligned, 0)

	return maxScore, vAligned, wAligned

if __name__ == '__main__':


	# Read the input data.
	with open(sys.argv[1]) as inputData:
		word1, word2 = [line.strip() for line in inputData.readlines()]

	# Get the alignment.
	alignment = global_alignment(word1, word2, BLOSUM62(), 5)

	# Print and save the answer.
	print '\n'.join(alignment)
	with open('output.txt', 'w') as outputData:
		outputData.write('\n'.join(alignment))