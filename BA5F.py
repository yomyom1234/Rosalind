import rosalind
from Bio.Align import substitution_matrices
import numpy as np

def find_max_value_and_position(array_2d):
	array_2d = np.array(array_2d)
	max_value = np.max(array_2d)
	max_indices = np.unravel_index(np.argmax(array_2d), array_2d.shape)
	return max_value, max_indices

def LocalAlignment(v, w, sigma, mat):
	len_v = len(v)
	len_w = len(w)
	s = np.zeros([len_v + 1, len_w + 1], dtype=np.int32)
	backtrack = np.full([len_v + 1, len_w + 1], "O")
	for i in range(1, len_v + 1):
		for j in range(1, len_w + 1):
			match = 0
			if v[i - 1] == w[j - 1]:
				match = 1
			s[i][j] = max(0,
						s[i - 1][j] + sigma,
						s[i][j - 1] + sigma,
						s[i - 1][j - 1] + mat[v[i - 1]][w[j - 1]])
			if (s[i][j] == 0):
				backtrack[i][j] == "O"
			elif (s[i][j] == s[i - 1][j - 1] + mat[w[j - 1]][v[i - 1]]):
				if match == 1:
					backtrack[i][j] = "M"
				else:
					backtrack[i][j] = "X"
			elif s[i][j] == s[i - 1][j] + sigma:
				backtrack[i][j] = "D"
			elif s[i][j] == s[i][j - 1] + sigma:
				backtrack[i][j] = "R"
	value, index = find_max_value_and_position(s)
	align_v = ""
	align_w = ""
	i = index[0]
	j = index[1]
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
		elif backtrack[i][j] == "O":
			i = 0
			j = 0
	if (i == 1 and j == 0):
		align_v = v[i - 1] + align_v
		align_w = "-" + align_w
	elif (i == 0 and j == 1):
		align_v = "-" + align_v
		align_w = w[j - 1] + align_w
	return align_v, align_w, value, backtrack

sequences = rosalind.read_data("./temp.txt")
v = sequences[0]
w = sequences[1]
mat = substitution_matrices.load("pam250")
align_v, align_w, value, back = LocalAlignment(v, w, -5, mat)
print(value)
print(align_v)
print(align_w)
