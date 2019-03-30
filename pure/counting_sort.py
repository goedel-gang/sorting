"""
Python in-place counting sort, adapted from
https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Counting_sort
"""

from sort_util import *

def _counting_sort(l, max_val):
    count = [0] * max_val
    for a in l:
        count[a] += 1
    i = 0
    for a in range(max_val):
        for c in range(count[a]):
            l[i] = a
            i += 1

def counting_sort(l):
    _counting_sort(l, max(l) + 1)

if __name__ == "__main__":
    main(counting_sort)
