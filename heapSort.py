def heapSort(aList):
	arr = aList[:]
	length = len(arr) - 1
	leastParent = length / 2
	for i in range (leastParent, -1, -1):
		moveDown(arr, i, length )

	for i in range (length, 0, -1):
		if arr[0] > arr[i]:
			swap(arr, 0, i)
			moveDown(arr, 0, i - 1)
	
	return arr


def moveDown(arr, first, last):
	largest = 2 * first + 1
	while largest <= last:
		if (largest < last) and (arr[largest] < arr[largest + 1]):
			largest += 1

		if arr[largest] > arr[first]:
			swap(arr, largest, first)
			first = largest;
			largest = 2 * first + 1
		else:
			return 


def swap(arr, a, b):
	arr[a], arr[b] = arr[b], arr[a]
