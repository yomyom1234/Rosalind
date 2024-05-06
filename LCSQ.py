import rosalind

def LongestCommonSubsequence(str1, str2):
	len_1 = len(str1)
	len_2 = len(str2)
	if len_1 > len_2:
		str2 = "0" * (len_1 - len_2) + str2
	elif len_2 > len_1:
		str1 = "0" * (len_2 - len_1) + str1
	len_1 = len(str1)
	len_2 = len(str2)
	LCS = [[0 for i in range(len_1)] for j in range(len_2)]
	for i in range(len_1):
		for j in range(len_2):
			if i == 0 or j == 0:
				LCS[i][j] == 0
			elif str1[i] == str2[j]:
				LCS[i][j] = LCS[i - 1][j - 1] + 1
			else:
				LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
	i = len_1 - 1
	j = len_2 - 1
	ret = []
	value = LCS[i][j]
	while (value != 0):
		if LCS[i - 1][j] == value:
			i = i - 1
		elif LCS[i][j - 1] == value:
			j = j - 1
		else:
			ret.append(str1[i])
			i = i - 1
			j = j - 1
			value = LCS[i][j]
	ret.reverse()
	string = ''.join(ret)
	return (string)

print(LongestCommonSubsequence("AACCTTGG", "ACACTGTGA"))
