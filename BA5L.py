import rosalind
from BA5K import MiddleEdge
import blosum as bl
import numpy as np
import copy
import time
import sys
sys.setrecursionlimit(10000000)

def LinearSequenceAlignment(v, w, top, bottom, left, right, sigma, mat, score, align_v, align_w):
#종료조건
#top == bottom, left == right이면 그냥 가로, 세로 출력하기
	print("v = ", v, " w = ", w, "top = ", top, " bottom = ", bottom, " left = ", left, " right = ", right)
	if top == bottom:
		score = score + (right - left) * sigma
		return score, align_v, align_w
	if left == right:
		score = score + (bottom - top) * sigma
		return score, align_v, align_w
#middle node 구하기
#middle edge 구하기
	len_v = len(v)
	len_w = len(w)
	middle = left + right // 2
	middle_node, middle_edge = MiddleEdge(v[top:bottom], w[left:right], sigma, mat)
	middle_node = [middle_node[0] + top, middle_node[1] + left]
	#print("middle_node = ", middle_node)
#0 ~ middle node까지 alignment 진행
	score, align_v, align_w = LinearSequenceAlignment(v, w, top, middle_node[0], left, middle_node[1], sigma, mat, score, align_v, align_w)
#middle edge 출력하기
	if middle_edge == 0:
		middle_node = [middle_node[0] + 1, middle_node[1]]
		score += sigma
	elif middle_edge == 1:
		score = score + mat[v[middle_node[0]]][w[middle_node[1]]]
		middle_node = [middle_node[0] + 1, middle_node[1] + 1]
	elif middle_edge == 2:
		middle_node = [middle_node[0], middle_node[1] + 1]
		score += sigma
#middle edge + 1 ~ 끝까지 alignment 진행
	score, align_v, align_w = LinearSequenceAlignment(v, w, middle_node[0], bottom, middle_node[1], right, sigma, mat, score, align_v, align_w)
	return score, align_v, align_w


sequences = rosalind.read_data("./temp.txt")
v = sequences[0]
w = sequences[1]
mat = bl.BLOSUM(62)
start = time.time()
print(LinearSequenceAlignment(v, w, 0, len(v), 0, len(w), -5, mat, 0, "", ""))
print(time.time() - start)
