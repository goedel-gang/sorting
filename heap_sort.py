def heap_sort(l):
    length = len(l) - 1
    least = length // 2

    for i in xrange(least, -1, -1):
        for xr in sift_down(l, i, length):
            yield xr

    for i in xrange(length, 0, -1):
        if l[0] > l[i]:
            yield 0, i
            l[0], l[i] = l[i], l[0]
            for xr in sift_down(l, 0, i - 1):
                yield xr

def sift_down(l, first, last):
    largest = 2 * first + 1
    while largest <= last:
        if largest < last and l[largest] < l[largest + 1]:
            yield largest,
            largest += 1

        if l[largest] > l[first]:
            yield largest, first
            l[largest], l[first] = l[first], l[largest]
            first = largest
            largest = 2 * first + 1
        else:
            break
