import rosalind
from BA1G import HammingDistance

def ApproximatePatternMatching(pattern, text, d):
	len_pattern = len(pattern)
	count = 0
	for i in range(len(text) - len_pattern + 1):
		if HammingDistance(text[i:i + len_pattern], pattern) <= d:
			count += 1
	return count
