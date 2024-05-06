import rosalind
import blosum as bl
import numpy as np

def GlobalAlignment(v, w, sigma, mat):
	len_v = len(v)
	len_w = len(w)
	s = np.zeros([len_v + 1, len_w + 1], dtype=np.int32)
	backtrack = np.full([len_v + 1, len_w + 1], "O")
	for i in range(1, len_v + 1):
		s[i][0] = s[i - 1][0] + sigma
	for j in range(1, len_w + 1):
		s[0][j] = s[0][j - 1] + sigma
	for i in range(1, len_v + 1):
		for j in range(1, len_w + 1):
			match = 0
			if v[i - 1] == w[j - 1]:
				match = 1
			s[i][j] = max(s[i - 1][j] + sigma,
						s[i][j - 1] + sigma,
						s[i - 1][j - 1] + mat[v[i - 1]][w[j - 1]])
			if (s[i][j] == s[i - 1][j - 1] + mat[w[j - 1]][v[i - 1]]):
				if match == 1:
					backtrack[i][j] = "M"
				else:
					backtrack[i][j] = "X"
			elif s[i][j] == s[i - 1][j] + sigma:
				backtrack[i][j] = "D"
			elif s[i][j] == s[i][j - 1] + sigma:
				backtrack[i][j] = "R"
	value = s[i][j]
	align_v = ""
	align_w = ""
	i = len_v
	j = len_w
	while ((i > 0) and (j > 0)):
		if backtrack[i][j] == "M" or backtrack[i][j] == "X":
			align_v = v[i - 1] + align_v
			align_w = w[j - 1] + align_w
			i -= 1
			j -= 1
		elif backtrack[i][j] == "D":
			align_v = v[i - 1] + align_v
			align_w = "-" + align_w
			i -= 1
		elif backtrack[i][j] == "R":
			align_v = "-" + align_v
			align_w = w[j - 1] + align_w
			j -= 1
	if (i == 1 and j == 0):
		align_v = v[i - 1] + align_v
		align_w = "-" + align_w
	elif (i == 0 and j == 1):
		align_v = "-" + align_v
		align_w = w[j - 1] + align_w
	for i in s:
		print(i)
	return align_v, align_w, value, backtrack


#sequences = rosalind.read_data("./temp.txt")
#v = sequences[0]
#w = sequences[1]
#mat = bl.BLOSUM(62)
#align_v, align_w, value, back = GlobalAlignment(v, w, -5, mat)
#print(value)
#print(align_v)
#print(align_w)
