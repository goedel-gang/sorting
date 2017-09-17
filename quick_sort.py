def partition(l, a, b):
    pivot = l[b]

    while True:
        while a < b and l[a] <= pivot:
            a += 1
            yield a,

        while a < b and l[b] > pivot:
            b -= 1
            yield b,

        if a < b:
            l[a], l[b] = l[b], l[a]
            yield a, b
        else:
            break
    yield b,

def _quick_sort(l, a, b):
    if a < b:
        for p in partition(l, a, b):
            yield p
        p, = p
        for i in _quick_sort(l, a, p - 1):
            yield i
        for i in _quick_sort(l, p, b):
            yield i

def quick_sort(l):
    return _quick_sort(l, 0, len(l) - 1)