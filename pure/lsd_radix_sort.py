"""
Least Significant Digit radix sort in Python. Modified to be in-place, and
simultaneously rewrite to list and fill buckets, so uses a little more
auxiliary space. Includes a wrapper to determine the max length.
"""

import itertools
import math

from sort_util import *

def _lsd_radix_sort(l, base, max_digits):
    bucks = [l]
    for power in range(max_digits):
        _bucks = [[] for i in range(base)]
        for ind, item in enumerate(itertools.chain.from_iterable(bucks)):
            l[ind] = item
            _bucks[(item // base ** power) % base].append(item)
        bucks = _bucks
    else:
        for ind, item in enumerate(itertools.chain.from_iterable(bucks)):
            l[ind] = item

def lsd_radix_sort(l, base=10):
    if l:
        max_digits = int(math.log(max(l), base) + 1)
        _lsd_radix_sort(l, base, max_digits)

if __name__ == "__main__":
    main(lsd_radix_sort)
