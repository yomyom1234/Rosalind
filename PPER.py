import rosalind
import math

def PartialPermutation(n, k):
	ret = math.perm(n, k)
	if (ret >= 1000000):
		ret %= 1000000
	return ret

sentences = rosalind.read_data("./temp.txt")
for sentence in sentences:
	if sentence :
		nums = sentence.split()
		print(PartialPermutation(int(nums[0]), int(nums[1])))
