'''
Find Frequent Words with Mismatches and Reverse Complements

Given: A string Text as well as integers k and d.
Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, PatternR) over all possible k-mers.

Given: 
ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1

Return:
ATGT ACAT

'''
import sys
import itertools

def mutations(word, hamming_distance, charset='ATCG'):
    # this enumerates all the positions in word
    #print word
    for indices in itertools.combinations( range( len( word ) ), hamming_distance ):
        #print "index:", indices
        for replacements in itertools.product(charset, repeat=hamming_distance):
            #print "\treplacements:", replacements
            mutation = list(word)
            for index, replacement in zip( indices, replacements ):
                #print "\t\t", index, ":", replacement
                mutation[ index ] = replacement
                #print "\t\t\t", mutation
            yield "".join( mutation )


with open(sys.argv[1]) as file:
	sequence = next(file).strip()
	kd = next(file).strip().split(' ')
	k = int(kd[0])
	mismatches = int(kd[1])

	#this is a list of all the kmers in the sequence
	kmers = []
	for i in range(0, len(sequence) - k + 1) :
		kmer = sequence[ i : i + k]
		kmers.append(kmer)

	counts = {}

	#for each kmer in the list of kmers
	for kmer in kmers: 
		current = []
		mygenerator = mutations(kmer, mismatches)
		for k in mygenerator:
			# print('\tk: ',k)
			if k not in counts:
				current.append(k)
				counts[k] = 1
			elif k not in current:
				current.append(k)
				counts[k] += 1

	max_count = 0
	max_kmers = []

	#test the reverse complements of the string
	for kmer, count in counts.items():
		k = kmer

		#? is used to help with the swap of characters
		k = k.replace('A','?')
		k = k.replace('T','A')
		k = k.replace('?','T')

		k = k.replace('C','?')
		k = k.replace('G','C')
		k = k.replace('?','G')
		k = k[::-1] #reverse string

		if k in counts:
			count += counts[k]
			
		if count > max_count:
			max_count = count
			max_kmers.clear()
			max_kmers.append(kmer)
		elif count == max_count:
			max_kmers.append(kmer)

	print(max_count)
	print(" ".join(max_kmers))