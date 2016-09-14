'''
Find the Most Frequent Words with Mismatches in a String

Given: A string Text as well as integers k and d.
Return: All most frequent k-mers with up to d mismatches in Text.

Given: 
ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1

Return:
GATG ATGC ATGT

'''
import itertools
import sys
import string
 
 
def count(genome, pattern, num_mismatches):
        i = 0
        count_p = 0
        while i <= len(genome) - len(pattern):
                indx = i
                count = 0
                for j in range(0, len(pattern)):
                        if genome[indx] == pattern[j]:
                                count = count + 1
                        indx = indx + 1
                if count >= len(pattern) - num_mismatches:
                        count_p = count_p + 1
               
                i = i + 1
        return count_p
'''        
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
'''

with open(sys.argv[1]) as file:

    sequence = next(file).strip()
    kd = next(file).strip().split(' ')
    kmer_size = int(kd[0])
    num_mismatches = int(kd[1])
    
    '''
    print("Read sequence = " + sequence)
    print("K-mer size = ", kmer_size)
    print("Max mismatches = ", num_mismatches)
    '''
     
    seq = "ATCG"
     
    ## Generate all possible kmers
     
    list_pattern = itertools.product(seq, repeat=kmer_size)

    max_p = 0
    aux = 0
    list_max = {}
    for p in list_pattern:
        aux = count(sequence, p, num_mismatches)
        #print("Analizing permutation... " , p)
        if aux >= max_p:
                max_p = aux
                list_max[p] = max_p
                #list_max.append([p, max_p])
    answers = []
    for l in list_max:
        if(list_max[l] == max_p):
            pat = ''
            for a in range(len(l)):
                pat += l[a]
            answers.append(pat)
            #print(pat, " ", list_max[l])

    print(' '.join(str(x) for x in answers))