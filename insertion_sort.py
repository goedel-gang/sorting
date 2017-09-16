def insertion_sort(l):
    for sorted_start in xrange(len(l)):
        val = l[sorted_start]
        for i in xrange(sorted_start, 0, -1):
            yield i, i - 1
            if l[i] < l[i - 1]:
                yield i, i - 1
                l[i], l[i - 1] = l[i - 1], l[i]
            else:
                break
