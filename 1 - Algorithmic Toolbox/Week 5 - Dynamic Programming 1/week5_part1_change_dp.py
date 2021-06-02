import sys

def get_change(money):
	coins = [1, 3, 4]
	change = [m for m in range(money + 1)] # most coins that could be used

	for m in range(money + 1):
		for c in coins:
			if c <= m: # coin that can be used to make change
				numCoins = change[m - c] + 1 # one more coin than prev optimal choice

				if numCoins <= change[m]: # if improves on current option
					change[m] = numCoins # is optimal choice

	return change[-1]
    

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
