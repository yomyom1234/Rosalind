import rosalind

def FindKmers(string, k):
	dict = {}
	len_string = len(string)
	for i in range(len_string - k + 1):
		if (string[i:i + k] in dict):
			dict[string[i:i + k]] += 1
		else:
			dict[string[i:i + k]] = 1
	return dict

def PatternCount(pattern, genome):
	len_pattern = len(pattern)
	count = 0
	for i in range(len(genome)):
		if (genome[i:i + len_pattern] == pattern):
			count += 1
	return count

def FindClump(string, k, L, t):
	len_string = len(string)
	kmers = FindKmers(string, k)
	kmers_list = [key for key, value in kmers.items() if value >= t]
	ret = []
	for i in range(len_string - L + 1):
		for pattern in kmers_list:
			if (PatternCount(pattern, string[i:i + L]) >= t) and not (pattern in ret):
				ret.append(pattern)
	return ret
