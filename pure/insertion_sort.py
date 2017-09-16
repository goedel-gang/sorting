"""
Insertion sort in Python, explicitly performing array swaps rather than letting
Python do the insertion.
"""

from sort_util import *

def insertion_sort(l):
    for sorted_start in range(len(l)):
        val = l[sorted_start]
        for i in range(sorted_start, 0, -1):
            if l[i] < l[i - 1]:
                l[i], l[i - 1] = l[i - 1], l[i]
            else:
                break

if __name__ == "__main__":
    main(insertion_sort)
