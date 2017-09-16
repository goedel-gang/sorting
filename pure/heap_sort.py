"""
In-place heapsort in Python, using pretty well-known algorithms.
"""

from sort_util import *

def heap_sort(l):
	length = len(l) - 1
	least = length // 2
	for i in range(least, -1, -1):
		sift_down(l, i, length)

	for i in range(length, 0, -1):
		if l[0] > l[i]:
			l[0], l[i] = l[i], l[0]
			sift_down(l, 0, i - 1)

def sift_down(l, first, last):
	largest = 2 * first + 1
	while largest <= last:
		if largest < last and l[largest] < l[largest + 1]:
			largest += 1

		if l[largest] > l[first]:
			l[largest], l[first] = l[first], l[largest]
			first = largest
			largest = 2 * first + 1
		else:
			break

if __name__ == "__main__":
    main(heap_sort)
