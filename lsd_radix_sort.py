import itertools
import math

def _lsd_radix_sort(l, base, max_digits):
    for power in xrange(max_digits):
        bucks = [[] for i in xrange(base)]
        for item in l:
            yield item,
            bucks[(item // base ** power) % base].append(item)
        for ind, val in enumerate(itertools.chain.from_iterable(bucks)):
            yield ind,
            l[ind] = val

def lsd_radix_sort(l, base=10):
    max_digits = int(math.log(max(l), base) + 1)
    return _lsd_radix_sort(l, base, max_digits)
