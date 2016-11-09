import sys

def BWT(word):
    '''Performs a Burrows-Wheeler transform on the given word.'''

    # Check that the word ends in the out of alphabet character '$'.
    word += ['', '$'][word[-1] != '$']

    # Store the length of the word to save a marginal amount of time, as we'll call the length often.
    wordLen = len(word)

    # A lambda function to get the nth character of the cyclic rotation (to the right) by i characters.
    rotationIndex = lambda i, n: word[(n-i) % wordLen]

    # A lambda function to compare cyclic rotations without generating the entire rotation.
    # Use the previously defined lambda function to compare rotation indices.
    comparator = lambda i, j, n=0: [1, -1][rotationIndex(i,n) < rotationIndex(j,n)] if rotationIndex(i,n) != rotationIndex(j,n) else comparator(i,j,n+1)

    # Sort the cyclic rotations based on their shift using the previously defined comparison function.
    sort = sorted(xrange(len(word)), cmp=comparator)

    # Return the last index of each cyclic rotation in the sorted oreder joined into a string.
    return ''.join([rotationIndex(i, -1) for i in sort])


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open(sys.argv[1]) as input_data:
        word = input_data.read().strip()

    # Get the Burrows-Wheeler Transform.
    bwt = BWT(word)

    # Print and save the answer.
    print(bwt)
    with open('output.txt', 'w') as output_data:
        output_data.write(bwt)

if __name__ == '__main__':
    main()