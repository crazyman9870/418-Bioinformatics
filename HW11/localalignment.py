import sys

from scripts import PAM250
from numpy import unravel_index, zeros


def localAlignment(v, w, scoringMatrix, sigma):
	'''Returns the score and local alignment with the given scoring matrix and indel penalty sigma for strings v, w.'''


	# Initialize the matrices.
	S = zeros((len(v)+1, len(w)+1), dtype=int)
	backtrack = zeros((len(v)+1, len(w)+1), dtype=int)

	# Fill in the Score and Backtrack matrices.
	for i in xrange(1, len(v)+1):
		for j in xrange(1, len(w)+1):
			scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoringMatrix[v[i-1], w[j-1]], 0]
			S[i][j] = max(scores)
			backtrack[i][j] = scores.index(S[i][j])

	# Quick lambda function to insert indels.
	insertIndel = lambda word, i: word[:i] + '-' + word[i:]

	# Get the position of the highest scoring cell in the matrix and the high score.
	i,j = unravel_index(S.argmax(), S.shape)
	maxScore = str(S[i][j])

	# Initialize the aligned strings as the input strings up to the position of the high score.
	vAligned, wAligned = v[:i], w[:j]

	# Backtrack to start of the local alignment starting at the highest scoring cell.
	while backtrack[i][j] != 3 and i*j != 0:
		if backtrack[i][j] == 0:
			i -= 1
			wAligned = insertIndel(wAligned, j)
		elif backtrack[i][j] == 1:
			j -= 1
			vAligned = insertIndel(vAligned, i)
		elif backtrack[i][j] == 2:
			i -= 1
			j -= 1

	# Cut the strings at the ending point of the backtrack.
	vAligned = vAligned[i:]
	wAligned = wAligned[j:]

	return maxScore, vAligned, wAligned

if __name__ == '__main__':

	# Read the input data.
	with open(sys.argv[1]) as inputData:
		word1, word2 = [line.strip() for line in inputData.readlines()]

	# Get the local alignment (given sigma = 5 in problem statement).
	alignment = localAlignment(word1, word2, PAM250(), 5)

	# Print and save the answer.
	print '\n'.join(alignment)
	with open('output.txt', 'w') as outputData:
		outputData.write('\n'.join(alignment))