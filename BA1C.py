import rosalind

seq = rosalind.read_data("./fasta.txt")
seq_list = list(seq[0])
seq_list.reverse()
seq = ''.join(seq_list)
print(rosalind.ComplementaryDNA(seq))
