"""
Quicksort in Python. Uses Hoare partitioning (although there's also a Lomuto
partition implementation) and a median-based pivot selection, and as few
high-level constructs as possible (no maps or filters or list comprehensions)
as they're generally unnecessary - the algorithm can be executed with single
passes.
"""

from sort_util import *

def lom_partition(l, a, b):
    pivot = l[b]
    i = a - 1    
    for j in range(a, b): 
        if l[j] < pivot:
            i += 1
            l[i], l[j] = l[j], l[i]

    if l[b] < l[i + 1]:
        l[i + 1], l[b] = l[b], l[i + 1]

    return i + 1

def partition(l, a, b):
    pivot = l[b]

    while True:
        while a < b and l[a] <= pivot:
            a += 1

        while a < b and l[b] > pivot:
            b -= 1

        if a < b:
            l[a], l[b] = l[b], l[a]
        else:
            return b

def _quick_sort(l, a, b):
    if a < b:
        p = partition(l, a, b)
        if p - 1 - a < b - p:
            _quick_sort(l, a, p - 1)
            _quick_sort(l, p, b)
        else:
            _quick_sort(l, p, b)
            _quick_sort(l, a, p - 1)

def quick_sort(l):
    _quick_sort(l, 0, len(l) - 1)

if __name__ == "__main__":
    main(quick_sort)
