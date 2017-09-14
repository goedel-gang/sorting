"""
Merge sort in Python. Ranges in this program are represented as an inclusive
start and a noninclusive stop. Does lots of in-place type stuff to optimise on
performance and allow visualisation.
"""

from sort_util import *

def merge(l, a_start, a_stop, b_start, b_stop):
    """
    Perform in-place merge on a list (using a temporary list to build merge.
    Takes start and stop parameters for the two segments to merge. Tries not to
    be too concise, in the interest of performance - rather than popping from
    lists it just explicitly iterates. Apart from some of the slicing (which
    can easily be emulated) this effectively only uses C-like functionality.
    """

    a_count = a_start
    b_count = b_start
    tmp = []

    while a_count < a_stop and b_count < b_stop:
        a_val, b_val = l[a_count], l[b_count]
        
        if a_val < b_val:
            tmp.append(a_val)
            a_count += 1
        else:
            tmp.append(b_val)
            b_count += 1

    tmp.extend(l[a_count:a_stop])
    tmp.extend(l[b_count:b_stop])

    l[a_start:b_stop] = tmp

def _merge_sort(l, start, stop):
    if stop - start > 1:
        mid = (start + stop) // 2
        _merge_sort(l, start, mid)
        _merge_sort(l, mid, stop)
        merge(l, start, mid, mid, stop)
    else:
        pass 

def merge_sort(l):
    _merge_sort(l, 0, len(l))

if __name__ == "__main__":
    args = get_args()
    test = randlist(args)
    if args.print:
        print(test)
    merge_sort(test)
    if args.print:
        print(test)
    print("sorted? = {}".format(is_sorted(test)))
