import itertools
import math

def _lsd_radix_sort(l, base, max_digits):
    bucks = [l]
    for power in xrange(max_digits):
        _bucks = [[] for i in xrange(base)]
        for ind, buckit in enumerate(itertools.chain.from_iterable(bucks)):
            yield ind,
            l[ind] = buckit
            _bucks[(buckit // base ** power) % base].append(buckit)
        bucks = _bucks
    else:
        for ind, val in enumerate(itertools.chain.from_iterable(bucks)):
            yield ind,
            l[ind] = val
        bucks = _bucks

def lsd_radix_sort(l, base=10):
    max_digits = int(math.log(max(l), base) + 1)
    return _lsd_radix_sort(l, base, max_digits)