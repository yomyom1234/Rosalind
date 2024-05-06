import rosalind

def MostFrequentKmer(string, k):
	dict = {}
	ret = []
	len_string = len(string)
	for i in range(len_string - k + 1):
		print(string[i:i + k])
		if (string[i:i + k] in dict):
			dict[string[i:i + k]] += 1
		else:
			dict[string[i:i + k]] = 1
	max_count = max(dict.values())
	keys = dict.keys()
	for seq in keys:
		if dict[seq] == max_count:
			ret.append(seq)
	return ret
