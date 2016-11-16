import sys

def DPChange(amount, coinList):
	'''Gives the minimum number of coins of denomination in coint_list necessary to create the given amount.'''
	# Initiate the amounts larger than zero as a number greater than the upper bound.
	minCoins = [0]+[(amount/min(coinList))+1]*amount
	# Use dynamic programming to build up to the desired amount.
	for m in range(1,amount+1):
		for coin in coinList:
			if m >= coin:
				if minCoins[m-coin] + 1 < minCoins[m]:
					minCoins[m] = minCoins[m-coin] + 1
	return minCoins[amount]

if __name__ == '__main__':

	# Read the input data.
	with open(sys.argv[1]) as input_data:
		money = int(input_data.readline().strip())
		coins = map(int, input_data.readline().strip().split(','))

	# Get the desired minimum number of coins.
	minCoins = str(DPChange(money, coins))

	# Print and save the answer.
	print minCoins
	with open('output.txt', 'w') as outputData:
		outputData.write(minCoins)