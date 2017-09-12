def merge(a, b):
	c = []
	while len(a) * len(b) > 0:
		if a[0] < b[0]:
			c.append(a.pop(0))
		else:
			c.append(b.pop(0))
	if len(b) == 0:
		c.extend(a)
	else:
		c.extend(b)
	return c

def mergeSort(arr):
	if len(arr) > 1:
		return merge(mergeSort(arr[:len(arr)//2]), mergeSort(arr[len(arr)//2:]))
	else:
		return arr

import random
import time
 
a = list(range(99999))
random.shuffle(a)

start = time.time()

msorted = mergeSort(a)

end = time.time()

print 'took {0} seconds'.format(end - start)

print 'it was {0}correct'.format('in' if msorted != sorted(a) else '')
