'''
Reconstruct a string from its Burrows-Wheeler transform.

Given: A string Transform (with a single "$" sign).
Return: The string Text such that BWT(Text) = Transform.

Given:
TTCCTAACG$A

Return:
TACATCACGT$
'''
import sys


def inverseBWT(bwt):
	'''Returns the inverse transform of the Burrows-Wheeler Transform bwt.'''

	# Enumerate the character order for repeat characters in the BWT and its sorted version.
	enumeratedBWT = enumerateWord(bwt)
	enumeratedSort = enumerateWord(sorted(bwt))

	# Construnct a mapping between the enumerated characters at each index of the enumerated BWT and sort.
	inverseDict = {enumeratedBWT[i]:enumeratedSort[i] for i in range(len(bwt))}

	# Construct the inverse BWT by a traversal through the inverse map.
	inverseBWT = ''
	current_char = enumeratedBWT[0]
	for i in range(len(bwt)):
		current_char = inverseDict[current_char]
		inverseBWT += current_char[0]

	# Shift the inverse BWT back one to get the correct starting point (since the inverse must end in '$').
	return inverseBWT[1:]+inverseBWT[0]


def enumerateWord(word):
	'''
	Enumerates like characters in the order of their appearance for the given word.
	i.e. 'abcbba' returns ['a0', 'b0', 'c0', 'b1', 'b2', 'a1']
	'''

	# Initialize the character count and enumerated character list.
	char_count = {}
	enumerated = []

	# Enumerate like characters.
	for ch in word:
		if ch not in char_count:
			char_count[ch] = 0
		else:
			char_count[ch] += 1
		enumerated.append(ch+str(char_count[ch]))

	return enumerated

def BWT(word):
	combos = []
	for i in range(len(word)):
		combos.append(word[i:] + word[:i])

	combos.sort()
	dolla = combos.pop(0)
	combos.append(dolla)

	#print('\n'.join(str(x) for x in combos))
	lastletters = []
	for combo in combos:
		lastletters.append(combo[len(combo)-1])

	#print('\n'.join(str(x) for x in lastletters))

	return lastletters

if __name__ == '__main__':

	with open(sys.argv[1]) as file:

		word = file.read().strip()

		# Construct the Inverse Burrows-Wheeler Transform.
		inverseBWT = inverseBWT(word)

		# Print and save the answer.
		print(inverseBWT)
		with open('output.txt', 'w') as outputFile:
			outputFile.write(inverseBWT)