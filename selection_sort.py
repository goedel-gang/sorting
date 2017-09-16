def selection_sort(l):
    for sort_size in xrange(len(l)):
        minind, minval = None, float("inf")
        for i in xrange(sort_size, len(l)):
            yield i,
            if l[i] < minval:
                minind, minval = i, l[i]
        yield sort_size, minind
        l[sort_size], l[minind] = l[minind], l[sort_size]
