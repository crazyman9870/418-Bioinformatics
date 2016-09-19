'''
Given: Integers k and t, followed by a collection of strings Dna.
Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t) with
pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string,
use the one occurring first.

Given:
3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG

Return:
TTC
ATC
TTC
ATC
TTC
'''

import sys
from greedymotifsearch import score, profileMostProbableKmer

def profilePseudocounts(motifs):
	'''Returns the profile of the dna list motifs.'''
	prof = []
	for i in range(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in range(len(motifs))])
		prof.append([float(col.count(nuc)+1)/float(len(col)+4) for nuc in 'ACGT'])
	return prof

def greedyMotifSearchAlgorithm(Dna, k, t):
    # Initialize the best score as a score higher than the highest possible score.
    bestScore = k*t

    # Run the greedy motif search.
    for i in range(len(Dna[0])-k+1):
        # Initialize the motifs as each k-mer from the first dna sequence.
        motifs = [Dna[0][i:i+k]]

        # Find the most probable k-mer in the next string.
        for j in range(1, t):
            currentProfile = profilePseudocounts(motifs)
            motifs.append(profileMostProbableKmer(Dna[j], k, currentProfile))

        # Check to see if we have a new best scoring list of motifs.
        currentScore = score(motifs)
        if currentScore < bestScore:
            bestScore = currentScore
            bestMotifs = motifs

    return bestMotifs

if __name__ == '__main__':

	with open(sys.argv[1]) as file:

		kt = next(file).strip().split()
		k = int(kt[0])
		t = int(kt[1])

		genomes = []
		for i in range(t):
			genomes.append(next(file).strip())

		kmers = greedyMotifSearchAlgorithm(genomes, k, t)

		print('\n'.join(str(x) for x in kmers))