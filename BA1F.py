import rosalind

def Prefix(string, i):
	return string[:i]

def GSubC(string):
	count_G = 0
	count_C = 0
	for i in string:
		if i == "C":
			count_C += 1
		elif i == "G":
			count_G += 1
	return count_G - count_C

def Skew(string):
	arr = []
	for i in range(len(string) + 1):
		prefix = Prefix(string, i)
		arr.append(GSubC(prefix))
	minimum = min(arr)
	for i in range(len(arr)):
		if arr[i] == minimum:
			print(i)
	return

Skew("ACTAAAGTGAGCATAATACGCGTCTCC")
