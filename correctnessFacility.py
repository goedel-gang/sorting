def test(sortFunc):
		
	import random

	print '\n{0}:'.format(sortFunc.__name__)

	a = list(range(10))

	allCorrect = True

	for i in range(1, 10):
		random.shuffle(a)
		if sortFunc(a) != sorted(a):
			allCorrect = False
			print '{0} became {1}!!'.format(a, sortFunc(a))
			break

	if not allCorrect:
		print 'NOT all correct'
	else:
		print 'all good'

import quickSort, mergeSort, insertSort, maxSort, bubbleSort, radixSort, heapSort, countingSort

test(countingSort.countingSort)
test(radixSort.radixSort)
test(quickSort.quickSort)
test(heapSort.heapSort)
test(mergeSort.mergeSort)
test(insertSort.insertSort)
test(maxSort.maxSort)
test(bubbleSort.bubbleSort)
