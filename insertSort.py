def insertSort(arr):
	out = []
	for i in arr:
		print len(out)
		for j in range(len(out)):
			if out[j] > i:
				out.insert(j, i)
				break
		else:
			out.append(i)
	
	return out

import random
import time
import sys

sys.setrecursionlimit(99999)
 
a = list(range(9999))
random.shuffle(a)

start = time.time()

msorted = insertSort(a)

end = time.time()

print 'took {0} seconds'.format(end - start)

print 'it was {0}correct'.format('in' if msorted != sorted(a) else '')
