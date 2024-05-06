import rosalind
import math

def Binominal(k, n):
	p = 0.25
	ret = 0
	num_of_child = 2**k

	for i in range(n, num_of_child + 1):
		ret += math.comb(num_of_child, i) * (p ** i) * ((1 - p) ** (num_of_child - i))
	return ret

print(Binominal(6, 18))
