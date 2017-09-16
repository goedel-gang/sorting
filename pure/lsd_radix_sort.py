"""
Least Significant Digit radix sort in Python.
"""

import itertools
import math

from sort_util import *

def _lsd_radix_sort(l, base, max_digits):
    for power in range(max_digits):
        bucks = [[] for i in range(base)]
        for item in l:
            bucks[(item // base ** power) % base].append(item)
        for ind, val in enumerate(itertools.chain.from_iterable(bucks)):
            l[ind] = val

def lsd_radix_sort(l, base=10):
    max_digits = int(math.log(max(l), base) + 1)
    _lsd_radix_sort(l, base, max_digits)

if __name__ == "__main__":
    main(lsd_radix_sort)
