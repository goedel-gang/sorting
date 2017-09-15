import itertools

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
        yield
        a_val, b_val = l[a_count], l[b_count]
        
        if a_val < b_val:
            tmp.append(a_val)
            a_count += 1
        else:
            tmp.append(b_val)
            b_count += 1

    for i in xrange(a_count, a_stop):
        yield
        tmp.append(l[i])

    for i in xrange(b_count, b_stop):
        yield
        tmp.append(l[i])

    for lindex, val in enumerate(tmp, a_start):
        yield
        l[lindex] = val

def _merge_sort(l, start, stop):
    if stop - start > 1:
        mid = (start + stop) // 2
        return itertools.chain(_merge_sort(l, start, mid),
                               _merge_sort(l, mid, stop),
                               merge(l, start, mid, mid, stop))
    else:
        return () 

def merge_sort(l):
    return _merge_sort(l, 0, len(l))
