import rosalind

codon_table = {'A' : 4, 'C' : 2, 'D' : 2, 'E' : 2, 'F' : 2, 'G' : 4, 'H' : 2, 'I' : 3, 'K' : 2, 'L' : 6, 'M' : 1, 'N' : 2, 'P' : 4, 'Q' : 2, 'R' : 6, 'S' : 6, 'T' : 4, 'V' : 4, 'W' : 1, 'Y' : 2}
sentences = rosalind.read_data("./data.txt")

def AAToNumOfPossibleSeqMod(input_string) :
	i = 0
	ret = 1
	count = 0;
	for aa in input_string:
		ret *= codon_table[aa]
		if (ret > 100000):
			count += 1
			ret %= 1000000
	ret *= 3
	if (ret > 100000):
		count += 1
	ret %= 1000000
	print(ret)

for sentence in sentences:
	calculate(sentence)
