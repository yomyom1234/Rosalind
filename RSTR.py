from scipy.stats import binom
import math

def GCSeqProbability(string, x):
	pGC = x / 2
	pAT = (1 - x) / 2
	count = {'A' : 0, 'T' : 0, 'G' : 0, 'C' : 0}
	for base in string:
		count[base] += 1
	ret = (count['G'] + count['C']) * math.log10(pGC) + (count['A'] + count['T']) * math.log10(pAT)
	return ret

def GCSeqProbabilityMultiple(N, x, string):
	pSingle = 10 ** GCSeqProbability(string, x)
	ret = 1 - ((1 - pSingle) ** N)
	return ret

print(GCSeqProbabilityMultiple(96304, 0.501639, 'CCCTCCAC'))
