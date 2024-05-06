import rosalind
from BA1H import ApproximatePatternMatching

def FrequentWordsWithMismatches(string, k, d):
	dict = {}
	ret = []
	kmers = rosalind.KmerGenerater(k)
	for i in kmers:
		dict[i] = 0
	for seq in dict.keys():
		dict[seq] += ApproximatePatternMatching(seq, string, d)
	max_count = max(dict.values())
	keys = dict.keys()
	for seq in keys:
		if dict[seq] == max_count:
			ret.append(seq)
	return ret
