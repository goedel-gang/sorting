def _bitonic_sort(l, a, b, up):
    if b - a > 1:
        mid = (a + b) // 2
        for xr in _bitonic_sort(l, a, mid, True):
            yield xr
        for xr in _bitonic_sort(l, mid, b, False):
            yield xr
        for xr in bitonic_merge(l, a, b, up):
            yield xr

def bitonic_merge(l, a, b, up):
    if b - a > 1:
        mid = (a + b) // 2
        for xr in bitonic_compare(l, a, b, up):
            yield xr
        for xr in bitonic_merge(l, a, mid, up):
            yield xr
        for xr in bitonic_merge(l, mid, b, up):
            yield xr

def bitonic_compare(l, a, b, up):
    dist = (b - a) // 2
    for i in range(a, a + dist):  
        yield i, i + dist
        if (l[i] > l[i + dist]) == up:
            yield i, i + dist
            l[i], l[i + dist] = l[i + dist], l[i]

def bitonic_sort(l):
    return _bitonic_sort(l, 0, len(l), True)