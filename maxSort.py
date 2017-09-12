def maxSort(arr):
	tarr = arr[:]
	if len(arr) > 1:
		m = max(arr)
		tarr.remove(m)
		return maxSort(tarr) + [m]
	else:
		return arr

import random
import time
import sys

sys.setrecursionlimit(99999)
 
a = list(range(9999))
random.shuffle(a)

start = time.time()

msorted = maxSort(a)

end = time.time()

print 'took {0} seconds'.format(end - start)

print 'it was {0}correct'.format('in' if msorted != sorted(a) else '')
