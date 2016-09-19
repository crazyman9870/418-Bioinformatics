'''
Given: Integers k and t, followed by a collection of strings Dna.
Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t). 
If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.

Given:
3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG

Return:
CAG
CAG
CAA
CAA
CAA

'''

import sys

def profileMostProbableKmer(Dna, k, profile):
    #Returns the profile most probable k-mer for the given input data.
    # A dictionary relating nucleotides to their position within the profile.
    nucLoc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}

    # Initialize the maximum probabily.
    maxProbability = -1

    # Compute the probability of the each k-mer, store it if it's currently a maximum.
    for i in range(len(Dna)-k+1):
        # Get the current probability.
        currentProbability = 1
        for j, nucleotide in enumerate(Dna[i:i+k]):
            currentProbability *= profile[j][nucLoc[nucleotide]]

        # Check for a maximum.
        if currentProbability > maxProbability:
            maxProbability = currentProbability
            mostProbable = Dna[i:i+k]

    return mostProbable

def score(motifs):
    #Returns the score of the given list of motifs.
    columns = [''.join(seq) for seq in zip(*motifs)]
    maxCount = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - maxCount


def profile(motifs):
    #Returns the profile of the dna list motifs.
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)) / float(len(col)) for nuc in 'ACGT'] for col in columns]

def greedyMotifSearchAlgorithm(Dna, k, t):
    # Initialize the best score as a score higher than the highest possible score.
    bestScore = k*t

    # Run the greedy motif search.
    for i in range(len(Dna[0])-k+1):
        # Initialize the motifs as each k-mer from the first dna sequence.
        motifs = [Dna[0][i:i+k]]

        # Find the most probable k-mer in the next string.
        for j in range(1, t):
            currentProfile = profile(motifs)
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