from random import randrange

def shuffle(x):
    for i in reversed(xrange(1, len(x))):
        j = randrange(i + 1)
        yield i, j
        x[i], x[j] = x[j], x[i]

def is_sorted(l):
    for i in xrange(len(l) - 1):
        yield i, i + 1
        if l[i] > l[i + 1]:
            yield False
            break
    else:
        yield True

def bogo_sort(l):
    while True:
        for i in shuffle(l):
            yield i
        for ind in is_sorted(l):
            if not isinstance(ind, bool):
                yield ind
            elif ind:
                break
