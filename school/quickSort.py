def quickSort(arr):
	if len(arr) > 1:
		pivot = arr[0]
		less = []
		greater = []
		equal = []
		for i in arr:
			if i == pivot:
				equal.append(i)
			elif i < pivot:
				less.append(i)
			else:
				greater.append(i)
		return quickSort(less) + equal + quickSort(greater)
	else:
		return arr

import random
import time
import sys

sys.setrecursionlimit(99999)
 
a = list(range(99999))
random.shuffle(a)

start = time.time()

msorted = quickSort(a)

end = time.time()

print 'took {0} seconds'.format(end - start)

print 'it was {0}correct'.format('in' if msorted != sorted(a) else '')
