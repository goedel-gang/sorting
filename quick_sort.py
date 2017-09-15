def partition(l, a, b):
    pivot = l[b]

    while True:
        while a < b and l[a] <= pivot:
            a += 1
            yield

        while a < b and l[b] > pivot:
            b -= 1
            yield

        if a < b:
            l[a], l[b] = l[b], l[a]
            yield
        else:
            break
    yield b

def _quick_sort(l, a, b):
    if a < b:
        for p in partition(l, a, b):
            yield
        for _ in _quick_sort(l, a, p - 1):
            yield
        for _ in _quick_sort(l, p, b):
            yield

def quick_sort(l):
    return _quick_sort(l, 0, len(l) - 1)