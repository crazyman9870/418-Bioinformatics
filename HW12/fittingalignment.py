import sys

def fittingAlignment(v,w):
    '''Returns the fitting alignment of strings v and w, along with the associated score.'''
    # Initialize the matrices.
    S = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    backtrack = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - 1, S[i][j-1] - 1, S[i-1][j-1] + [-1, 1][v[i-1] == w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Get the position of the highest scoring cell corresponding to the end of the shorter word w.
    j = len(w)
    i = max(enumerate([S[row][j] for row in xrange(len(w), len(v))]),key=lambda x: x[1])[0] + len(w)
    maxScore = str(S[i][j])

    # Initialize the aligned strings as the input strings up to the position of the high score.
    vAligned, wAligned = v[:i], w[:j]

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Backtrack to start of the fitting alignment.
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            wAligned = insert_indel(wAligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            vAligned = insert_indel(vAligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut off v at the ending point of the backtrack.
    vAligned = vAligned[i:]

    return maxScore, vAligned, wAligned

if __name__ == '__main__':

    # Read the input data.
    with open(sys.argv[1]) as inputData:
        word1, word2 = [line.strip() for line in inputData.readlines()]

    # Get the fitting alignment.
    alignment = fittingAlignment(word1, word2)

    # Print and save the answer.
    print '\n'.join(alignment)
    with open('output.txt', 'w') as outputData:
        outputData.write('\n'.join(alignment))