"""
Bitonic sort lifted from wikipedia:
https://en.wikipedia.org/wiki/Bitonic_sorter and adapted to be in-place, and
hacked into a messy version that will extend to non-power of two.
"""

from sort_util import *

def _bitonic_sort(l, a, b, up, maxind):
    if a < maxind and b - a > 1:
        mid = (a + b) // 2
        _bitonic_sort(l, a, mid, True, maxind)
        _bitonic_sort(l, mid, b, False, maxind)
        bitonic_merge(l, a, b, up)

def bitonic_merge(l, a, b, up):
    if b - a > 1:
        mid = (a + b) // 2
        bitonic_compare(l, a, b, up)
        bitonic_merge(l, a, mid, up)
        bitonic_merge(l, mid, b, up)

def bitonic_compare(l, a, b, up):
    dist = (b - a) // 2
    for i in range(a, a + dist):  
        if (l[i] > l[i + dist]) == up:
            l[i], l[i + dist] = l[i + dist], l[i]

def bitonic_sort(l):
    next_pow = 1 << (len(l) - 1).bit_length()
    l.extend(float("inf") for _ in range(next_pow - len(l)))
    _bitonic_sort(l, 0, len(l), True, len(l))

if __name__ == "__main__":
    main(bitonic_sort)
