import rosalind

def FindingLCS(sequences):
	short = min(sequences, key=len)
	substring_array = makeSubstringArray(short)
	for sub in substring_array:
		flag = True
		for seq in sequences:
			if not (sub in seq):
				flag = False
				break
		if flag == True:
			print(sub)
			break
	return (substring_array)

def makeSubstringArray(string):
	arr = []
	len_string = len(string)
	for i in range(len_string, 1, -1):
		for j in range(len_string - i + 1):
			arr.append(string[j:j + i])
	return arr
