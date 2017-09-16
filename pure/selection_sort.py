"""
Selection sort in Python, performing a swap after a max pass
"""

from sort_util import *

def selection_sort(l):
    for sort_size in range(len(l)):
        minind, minval = None, float("inf")
        for i in range(sort_size, len(l)):
            if l[i] < minval:
                minind, minval = i, l[i]
        l[sort_size], l[minind] = l[minind], l[sort_size]

if __name__ == "__main__":
    main(selection_sort)
