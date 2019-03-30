"""
Smoothsort in Python, with code taken from
https://github.com/toroidal-code/smoothsort-py/blob/master/smoothsort.py.
"""

from sort_util import *

def sift(arr, r1, b1, c1):
    r0 = r1
    T = arr[r0]
    while b1 >= 3:
        r2 = r1 - b1 + c1
        if not arr[r1 - 1] <= arr[r2]:
            r2 = r1 - 1
            b1, c1 = c1, b1 - c1 - 1
        if arr[r2] <= T:
            b1 = 1
        else:
            arr[r1] = arr[r2]
            r1 = r2
            b1, c1 = c1, b1 - c1 - 1
    if r1 != r0:
        arr[r1] = T
    return arr, r1, b1, c1

def trinkle(arr, p, b1, c1, b, c, r, r1):
    p1 = p
    b1 = b
    c1 = c
    r0 = r1
    T = arr[r0]
    while p1 > 0:
        while (p1 & 1) == 0:
            p1 >>= 1
            b1, c1 = b1 + c1 + 1, b1
        r3 = r1 - b1
        if p1 == 1 or arr[r3] <= T:
            p1 = 0
        else:
            p1 -= 1
            if b1 == 1:
                arr[r1] = arr[r3]
                r1 = r3
            elif b1 >= 3:
                r2 = r1 - b1 + c1
                if not arr[r1 - 1] <= arr[r2]:
                    r2 = r1 - 1
                    b1, c1 = c1, b1 - c1 - 1
                    p1 <<= 1
                if arr[r2] <= arr[r3]:
                    arr[r1] = arr[r3]
                    r1 = r3
                else:
                    arr[r1] = arr[r2]
                    r1 = r2
                    b1, c1 = c1, b1 - c1 - 1
                    p1 = 0
    if r0 != r1:
        arr[r1] = T
    arr, r1, b1, c1 = sift(arr, r1, b1, c1)
    return arr, p, b1, c1, b, c, r, r1

def semitrinkle(arr, p, b1, c1, b, c, r, r1):
    r1 = r - c
    if not arr[r1] <= arr[r]:
        arr[r], arr[r1] = arr[r1], arr[r]
        arr, p, b1, c1, b, c, r, r1 = trinkle(arr, p, b1, c1, b, c, r, r1)
    return arr, p, b1, c1, b, c, r, r1

def smooth_sort(arr):
    """
    The main Smooth_sort function
    Variables: q,r,p,b,c,r1,b1,c1,N
    """

    # Start of main function
    N = len(arr)
    q = 1
    r = 0
    p = 1
    b = 1
    c = 1
    #building the tree
    while q < N:
        r1 = r

        if (p & 7) == 3:
            b1 = b
            c1 = c
            arr, r1, b1, c1 = sift(arr, r1, b1, c1)
            p = (p + 1) >> 2
            b, c = b + c + 1, b
            b, c = b + c + 1, b
        elif (p & 3) == 1:
            if (q + c) < N:
                b1 = b
                c1 = c
                arr, r1, b1, c1 = sift(arr, r1, b1, c1)
            else:
                arr, p, b1, c1, b, c, r, r1 = trinkle(arr, p, b1, c1, b, c, r, r1)
            b, c = c, b - c - 1
            p <<= 1
            while b > 1:
                b, c = c, b - c - 1
                p <<= 1
            p += 1
        q += 1
        r += 1

    r1 = r
    arr, p, b1, c1, b, c, r, r1 = trinkle(arr, p, b1, c1, b, c, r, r1)

    #build the sorted array
    while q > 1:
        q -= 1
        if b == 1:
            r -= 1
            p -= 1
            while (p & 1) == 0:
                p >>= 1
                b, c = b + c + 1, b
        elif b >= 3:
            p -= 1
            r = r - b + c
            if p > 0:
                arr, p, b1, c1, b, c, r, r1 = semitrinkle(arr, p, b1, c1, b, c, r, r1)
            b, c = c, b - c - 1
            p = (p << 1) + 1
            r += c
            arr, p, b1, c1, b, c, r, r1 = semitrinkle(arr, p, b1, c1, b, c, r, r1)
            b, c = c, b - c - 1
            p = (p << 1) + 1
            # element q is done
            # element 0 is done

if __name__ == "__main__":
    main(smooth_sort)
