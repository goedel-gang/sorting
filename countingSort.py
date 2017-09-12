def countingSort(aList):
	arr = aList[:]
	k = len(arr)
	counter = [0] * (k + 1)
	for i in arr:
		counter[i] += 1

	index = 0;
	for i in range(len(counter)):
		while 0 < counter[i]:
			arr[index] = i
			index += 1
			counter[i] -= 1
	return arr

#def assumptionSort(arr):
#	'''with the assumption that this is a set of consecutive distinct integers - approached from just common sense and also from countingSort'''
#	return range(len(arr))
