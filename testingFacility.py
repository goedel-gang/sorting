def test(sortFunc, takesArg=True):
		
	import random, time, sys, multiprocessing

	print '{0}:'.format(sortFunc.__name__)

	sys.setrecursionlimit(99999)

	for i in range(1, 20):
		size = 10**i
		print 'testing size {0} (10**{1})'.format(size, i)

		times = []
		if takesArg:
			a = list(range(size))

		for _ in range(6):
			if takesArg:
				random.shuffle(a)
				f = multiprocessing.Process(target=sortFunc, name='sortFunc', args=(a,))
			else:
				f = multiprocessing.Process(target=sortFunc, name='sortFunc')
				
			start = time.time()
			f.start()
			f.join(16)
			end = time.time()

			if f.is_alive():
				f.terminate()
			if end - start > 15:
				times.append('>15')
				break
			else:
				times.append(end - start)

		print 'the times were {0},\naveraging {1}\n'.format(times, '>15' if '>15' in times else sum(times)/len(times))

		if '>15' in times:
			break

import quickSort, mergeSort, insertSort, maxSort, bubbleSort, radixSort, heapSort, countingSort, bucketSort

test(countingSort.countingSort)
test(radixSort.radixSort)
test(quickSort.quickSort)
test(heapSort.heapSort)
test(mergeSort.mergeSort)
test(bucketSort.bucketSort)
test(insertSort.insertSort)
test(maxSort.maxSort)
test(bubbleSort.bubbleSort)
