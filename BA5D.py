import rosalind

def MakeWeightArray(strings, num_nodes):
	weights = [[0 for i in range(num_nodes)] for j in range(num_nodes)]
	for string in strings:
		if string != '':
			numbers = string.replace('->', ':').split(':')
			#numbers = string.split(' ')
			num_from, num_to, weight = map(int, numbers)
			weights[num_from][num_to] = weight
	for i in weights:
		print(i)
	path = [0 for i in range(num_nodes)]
	value = [0 for i in range(num_nodes)]
	flag = [1 for i in range(num_nodes)]
	for j in range(1, num_nodes):
		if CheckConnection(weights, j) == False:
			flag[j] = -1
		col_flag = -1
		for i in range(0, num_nodes):
			if weights[i][j] > 0:
				if ((value[i] + weights[i][j]) > value[j]) and (flag[i] > 0):
					value[j] = value[i] + weights[i][j]
					path[j] = i
					col_flag = 1
		flag[j] = col_flag
	return flag, path, value

def CheckConnection(weights, j):
	has_positive = any(weights[row][j] > 0 for row in range(len(weights[0])))
	return has_positive

def Backtraking(path, value, num_nodes):
	arr = []
	i = num_nodes - 1
	arr.append(i)
	while (i != 0):
		arr.append(path[i])
		i = path[i]
	arr.reverse()
	end = arr[-1]
	string = ""
	for i in arr:
		string = string + str(i)
		if (i != end):
			string = string + "->"
	length = value[-1]
	return length, string

strings = rosalind.read_data("./temp.txt")
flag, path, value = MakeWeightArray(strings[2:], int(strings[1]) + 1)
len, ret = Backtraking(path, value, int(strings[1]) + 1)
print("---------")
print(flag)
print(path)
print(value)
print(len)
print(ret)
