import rosalind
from BA5K import MiddleEdge
import blosum as bl
import numpy as np
import copy
import time
import sys
sys.setrecursionlimit(10000000)

def LinearSequenceAlignment(x, v, w, top, bottom, left, right, sigma, mat, score, align_v, align_w):
#종료조건
#top == bottom, left == right이면 그냥 가로, 세로 출력하기
	if top == bottom:
		score = score + (right - left) * sigma
		align_v += ("-" * (right - left))
		align_w += w[left:right]
		return score, align_v, align_w
	if left == right:
		score = score + (bottom - top) * sigma
		align_v += v[top:bottom]
		align_w += ("-" * (bottom - top))
		return score, align_v, align_w
#middle node 구하기
#middle edge 구하기
	middle_node, middle_edge = MiddleEdge(v[top:bottom], w[left:right], sigma, mat)
	middle_node = [middle_node[0] + top, middle_node[1] + left]
#0 ~ middle node까지 alignment 진행
	score, align_v, align_w = LinearSequenceAlignment(x + 1, v, w, top, middle_node[0], left, middle_node[1], sigma, mat, score, align_v, align_w)
#middle edge 출력하기
	#down
	if middle_edge == 0:
		score += sigma
		align_v += v[middle_node[0]]
		align_w += "-"
		middle_node = [middle_node[0] + 1, middle_node[1]]
	#diag
	elif middle_edge == 1:
		score = score + mat[v[middle_node[0]]][w[middle_node[1]]]
		align_v += v[middle_node[0]]
		align_w += w[middle_node[1]]
		middle_node = [middle_node[0] + 1, middle_node[1] + 1]
	#right
	elif middle_edge == 2:
		score += sigma
		align_v += "-"
		align_w += w[middle_node[1]]
		middle_node = [middle_node[0], middle_node[1] + 1]
#middle edge + 1 ~ 끝까지 alignment 진행
	score, align_v, align_w = LinearSequenceAlignment(x + 1, v, w, middle_node[0], bottom, middle_node[1], right, sigma, mat, score, align_v, align_w)
	return score, align_v, align_w


sequences = rosalind.read_data("./temp.txt")
v = sequences[0]
w = sequences[1]
mat = bl.BLOSUM(62)
start = time.time()
score, align_v, align_w = LinearSequenceAlignment(0, v, w, 0, len(v), 0, len(w), -5, mat, 0, "", "")
print(score)
print(align_v)
print(align_w)
print(time.time() - start)
