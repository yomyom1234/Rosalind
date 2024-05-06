import rosalind
from BA1H import ApproximatePatternMatching

def FrequentWordsWithMismatches(string, k, d, kmers):
	dict = {}
	ret = []
	for i in kmers:
		dict[i] = 0
	for seq in dict.keys():
		dict[seq] += ApproximatePatternMatching(seq, string, d)
	return dict

def FrequentWordsWithMismatchesAndReverseComplements(string, k, d):
	ret = []
	kmers = rosalind.KmerGenerater(k)
	string_RC = rosalind.ReverseComplementaryDNA(string)
	dict_1 = FrequentWordsWithMismatches(string, k, d, kmers)
	dict_2 = FrequentWordsWithMismatches(string_RC, k, d, kmers)
	dict_complete = {}
	for i in dict_1.keys():
		dict_complete[i] = dict_1[i] + dict_2[i]
	max_count = max(dict_complete.values())
	keys = dict_complete.keys()
	for seq in keys:
		if dict_complete[seq] == max_count:
			ret.append(seq)
	return ret
