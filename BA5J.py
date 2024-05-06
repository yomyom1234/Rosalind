import rosalind
import blosum as bl
import numpy as np

def AffineGapAlignment(v, w, sigma, epsilon, mat):
	len_v = len(v)
	len_w = len(w)
	lower = np.zeros([len_v + 1, len_w + 1], dtype=np.int32)
	middle = np.zeros([len_v + 1, len_w + 1], dtype=np.int32)
	upper = np.zeros([len_v + 1, len_w + 1], dtype=np.int32)
	backtrack_l = np.full([len_v + 1, len_w + 1], "0")
	backtrack_m = np.full([len_v + 1, len_w + 1], "0")
	backtrack_u = np.full([len_v + 1, len_w + 1], "0")
	for i in range(1, len_v + 1):
		lower[i][0] = lower[i - 1][0] + epsilon
		upper[i][0] = upper[i - 1][0] + epsilon
	for j in range(1, len_w + 1):
		lower[0][j] = lower[0][j - 1] + epsilon
		upper[0][j] = upper[0][j - 1] + epsilon
	for i in range(1, len_v + 1):
		for j in range(1, len_w + 1):
			match = 0
			if v[i - 1] == w[j - 1]:
				match = 1
			lower[i][j] = max(lower[i - 1][j] + epsilon,
							middle[i - 1][j] + sigma)
			upper[i][j] = max(upper[i][j - 1] + epsilon,
							middle[i][j - 1] + sigma)
			middle[i][j] = max(lower[i][j],
							middle[i - 1][j - 1] + mat[v[i - 1]][w[j - 1]],
							upper[i][j])

			#backtrack for middle
			if (middle[i][j] == middle[i - 1][j - 1] + mat[v[i - 1]][w[j - 1]]):
				if match == 1:
					backtrack_m[i][j] = "M"
				else:
					backtrack_m[i][j] = "X"
			elif (middle[i][j] == lower[i][j]):
				backtrack_m[i][j] = "l"
			elif (middle[i][j] == upper[i][j]):
				backtrack_m[i][j] = "u"

			#backtrack for lower
			if (lower[i][j] == lower[i - 1][j] + epsilon):
				backtrack_l[i][j] = "D"
			elif (lower[i][j] == middle[i - 1][j] + sigma):
				backtrack_l[i][j] = "m"

			#backtrack for upper
			if (upper[i][j] == upper[i][j - 1] + epsilon):
				backtrack_u[i][j] = "R"
			elif (upper[i][j] == middle[i][j - 1] + sigma):
				backtrack_u[i][j] = "m"

	score = middle[len_v][len_w]
	align_v = ""
	align_w = ""

	#Backtracking
	backs = [backtrack_l, backtrack_m, backtrack_u]
	pointer = 1
	i = len_v
	j = len_w
	while ((i > 0) and (j > 0)):
		backtrack = backs[pointer]
		if pointer == 0:
			if backtrack[i][j] == "D":
				align_v = v[i - 1] + align_v
				align_w = "-" + align_w
				i -= 1
			elif backtrack[i][j] == "m":
				pointer = 1
				align_v = v[i - 1] + align_v
				align_w = "-" + align_w
				i -= 1
		elif pointer == 1:
			if backtrack[i][j] == "M" or backtrack[i][j] == "X":
				align_v = v[i - 1] + align_v
				align_w = w[j - 1] + align_w
				i -= 1
				j -= 1
			elif backtrack[i][j] == "l":
				pointer = 0
			elif backtrack[i][j] == "u":
				pointer = 2
		elif pointer == 2:
			if backtrack[i][j] == "R":
				align_v = "-" + align_v
				align_w = w[j - 1] + align_w
				j -= 1
			elif backtrack[i][j] == "m":
				pointer = 1
				align_v = "-" + align_v
				align_w = w[j - 1] + align_w
				j  -= 1


	if (i == 1 and j == 0):
		align_v = v[i - 1] + align_v
		align_w = "-" + align_w
	elif (i == 0 and j == 1):
		align_v = "-" + align_v
		align_w = w[j - 1] + align_w

	#print("---------lower score---------")
	#max_width = max(len(str(item)) for row in lower for item in row)
	#for i in lower:
	#	print(" ".join(f"{item:>{max_width}}" for item in i))
	#print("---------lower back---------")
	#for i in backtrack_l:
	#	print(i)
	#print("---------middle score---------")
	#max_width = max(len(str(item)) for row in middle for item in row)
	#for i in middle:
	#	print(" ".join(f"{item:>{max_width}}" for item in i))
	#print("---------middle back---------")
	#for i in backtrack_m:
	#	print(i)
	#print("---------upper score---------")
	#max_width = max(len(str(item)) for row in upper for item in row)
	#for i in upper:
	#	print(" ".join(f"{item:>{max_width}}" for item in i))
	#print("---------upper back---------")
	#for i in backtrack_u:
	#	print(i)
	return score, align_v, align_w


mat = bl.BLOSUM(62)
sequences = rosalind.read_data("./temp.txt")
v = sequences[0]
w = sequences[1]

score, align_v, align_w = AffineGapAlignment(v, w, -11, -1, mat)

print(score)
print(align_v)
print(align_w)
