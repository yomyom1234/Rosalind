import rosalind
import blosum as bl
import numpy as np
import copy
import time

def CalculateOnlyScore(v, w, sigma, mat):
	len_v = len(v)
	len_w = len(w)
	previous = np.arange(0, (len_v + 1) * sigma, sigma)
	current = np.arange(0, (len_v + 1) * sigma, sigma)
	score_matrix = np.array([mat[vi][wi] for wi in w for vi in v], dtype=np.int32).reshape(len_w, len_v)
	for i in range(len_w):
		current[0] = sigma * (i + 1)
		for j in range(1, len_v + 1):
			temp_list = [current[j - 1] + sigma, previous[j - 1] + score_matrix[i][j - 1], previous[j] + sigma]
			current[j] = max(temp_list)
		previous, current = current, previous
	return previous

def CalculateScoreWithLastEdge(v, w, sigma, mat):
	len_v = len(v)
	len_w = len(w)
	previous = np.arange(0, (len_v + 1) * sigma , sigma)
	current = np.arange(0, (len_v + 1) * sigma, sigma)
	direction = np.full(len_v + 1, 2, dtype=np.int32)
	score_matrix = np.array([mat[vi][wi] for wi in w for vi in v], dtype=np.int32).reshape(len_w, len_v)
	for i in range(len_w):
		current[0] = sigma * (i + 1)
		for j in range(1, len_v + 1):
			temp_list = [current[j - 1] + sigma, previous[j - 1] + score_matrix[i][j - 1], previous[j] + sigma]
			current[j] = max(temp_list)
			direction[j] = temp_list.index(current[j])
		previous, current = current, previous
	return (previous, direction)

def MiddleEdge(v, w, sigma, mat):
	len_v = len(v)
	len_w = len(w)
	middle = len_w // 2
	left_list = CalculateOnlyScore(v, w[:middle], sigma, mat)
	right_list, dir = CalculateScoreWithLastEdge(v[::-1], w[middle:][::-1], sigma, mat)
	score_list = left_list + right_list[::-1]
	middle_node = [np.argmax(score_list),middle]
	dir = dir[::-1]
	return (middle_node, dir[middle_node[0]])

#v = "PLEA"
#w = "M"
#mat = bl.BLOSUM(62)
#start = time.time()
#print(MiddleEdge(v, w, -5, mat))
#print(time.time() - start)
