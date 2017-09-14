def bubbleSort(arr):
	j = 1
	out = arr[:]
	hasSwapped = True
	while hasSwapped:
		hasSwapped = False
		for i in range(len(out) - j):
			if out[i] > out[i+1]:
				out[i], out[i+1] = out[i+1], out[i]
				hasSwapped = True
		j += 1

	return out

#import random
#import time
#import sys

#sys.setrecursionlimit(99999)
# 
#a = list(range(9999))
#random.shuffle(a)

#start = time.time()

#msorted = bubbleSort(a)

#end = time.time()

#print 'took {0} seconds'.format(end - start)

#print 'it was {0}correct'.format('in' if msorted != sorted(a) else '')
