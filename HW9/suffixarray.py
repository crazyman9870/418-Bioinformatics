import sys

def constructSuffixArray(word):
	'''Constructs a suffix array from the given word.'''

	# Check that the word ends in the out of alphabet character '$'.
	word += ['', '$'][word[-1] != '$']

	# A lambda function to compare suffixes without generating the entire suffix.
	# Idea: To compare the suffixes word[i:] and word[j:] compare the letter at the ith and jth index.
	#       Return -1 if the ith letter comes before the jth letter, 1 if jth letter comes before the ith letter.
	#       If the indices match, repeat the process with the letter at the (i+1)th and (j+1)th index.
	comparator = lambda i,j: [1, -1][word[i] < word[j]] if word[i] != word[j] else comparator(i+1,j+1)

	# Sort the integer array using the suffix comparison function.
	suffixArray = sorted(xrange(len(word)), cmp=comparator)

	return suffixArray


def main():
	'''Main call. Reads, runs, and saves problem specific data.'''

	# Read the input data.
	with open(sys.argv[1]) as inputData:
		text = inputData.read().strip()

	# Construct the suffix array and map the elements to a string for output writing.
	suffixArray = map(str, constructSuffixArray(text))

	# Print and save the answer.
	print(', '.join(suffixArray))
	with open('output.txt', 'w') as output_data:
		output_data.write(', '.join(suffixArray))


if __name__ == '__main__':
	main()