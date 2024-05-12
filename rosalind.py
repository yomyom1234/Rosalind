import itertools

def read_data(file_name):
	with open(file_name, 'r') as file:
		content = file.read()

	sentences = content.split('\n')
	return sentences

def read_FASTA(file_name):
	sentences = read_data(file_name)
	result = []
	i = 0
	new = ""
	for sentence in sentences:
		if sentence != '':
			if sentence[0] == '>':
				result.append(new)
				new = ""
			else:
				new = new + sentence
	return result[1:]

def write_List_Data(file_name, list):
	file = open(file_name, 'w')
	for sentence in list:
		file.write(str(sentence))
		file.write('\n')
	file.close()

def write_Data(file_name, data):
	file = open(file_name, 'w')
	file.write(str(data))
	file.write('\n')
	file.close

def ReverseComplementaryDNA(str):
	newstr = ""
	for seq in str:
		if seq == "A":
			newstr = newstr + "T"
		elif seq == "T":
			newstr = newstr + "A"
		elif seq == "C":
			newstr = newstr + "G"
		elif seq == "G":
			newstr = newstr + "C"
	newstr_list = list(newstr)
	newstr_list.reverse()
	ret = ''.join(newstr_list)
	return ret

def SeqToAA(str):
	codon_table = {"TTT" : "F", "TTC" : "F",
	"TTA" : "L", "TTG" : "L", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L",
	"ATT" : "I", "ATC" : "I", "ATA" : "I",
	"ATG" : "M",
	"GTT" : "V", "GTC" : "V", "GTA" : "V", "GTG": "V",
	"TCT" : "S", "TCC" : "S", "TCA" : "S", "TCG" : "S", "AGT" : "S", "AGC" : "S",
	"CCT": "P", "CCC": "P", "CCA": "P", "CCG" : "P",
	"ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T",
	"GCT" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A",
	"TAT" : "Y",  "TAC" : "Y",
	"TAA" : "STOP",  "TAG" : "STOP",  "TGA" : "STOP",
	"CAT" : "H", "CAC" : "H",
	"CAA" : "Q", "CAG" : "Q",
	"AAT" : "N", "AAC" : "N",
	"AAA" : "K", "AAG" : "K",
	"GAT" : "D", "GAC" : "D",
	"GAA" : "E", "GAG" : "E",
	"TGT" : "C", "TGC" : "C",
	"TGG" : "W",
	"CGT" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "AGA" : "R", "AGG" : "R",
	"GGT" :"G", "GGC" :"G", "GGA" :"G", "GGG" : "G"}
	return codon_table[str]

def KmerGenerater(k):
	bases = ["A", "T", "G", "C"]
	kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]
	return kmers
