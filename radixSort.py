def radixSort(arr):
	out = arr
	radx = 10
	maxLength = False
	tmp, placement = -1, 1

	while not maxLength:
		maxLength = True
		buckets = [list() for _ in range( radx )]
		for i in out:
			tmp = i / placement
			buckets[tmp % radx].append( i )
			if maxLength and tmp > 0:
				maxLength = False
		a = 0
		for i in range( radx ):
			buck = buckets[i]
			for j in buck:
				out[a] = j
				a += 1
		placement *= radx
	return out
