import rosalind

def DPChange(money, coins):
	MinNumCoins = [0 for i in range(money + 1)]
	for m in range(1, money + 1):
		MinNumCoins[m] = 2147483648
		for i in range(len(coins)):
			if m >= coins[i]:
				if MinNumCoins[m - coins[i]] + 1 < MinNumCoins[m]:
					MinNumCoins[m] = MinNumCoins[m - coins[i]] + 1
	return MinNumCoins[money]

print(DPChange(16699, [1, 3, 5, 24]))
