def _counting_sort(l, max_val):
    count = [0] * max_val
    for ind, a in enumerate(l):
        yield ind,
        count[a] += 1
    i = 0
    for a in range(max_val):
        for c in range(count[a]):
            yield i,
            l[i] = a
            i += 1

def counting_sort(l):
	return _counting_sort(l, max(l) + 1)