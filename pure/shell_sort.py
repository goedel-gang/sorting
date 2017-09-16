"""
Shell sort in Python. Using the algorithm and gaps from Wikipedia.
"""

from sort_util import *

GAPS = [701, 301, 132, 57, 23, 10, 4, 1]

def shell_sort(l):
    for gap in GAPS:
        for i in range(len(l)):
            for j in range(i, gap - 1, -gap):
                if l[j] < l[j - gap]:
                    l[j], l[j - gap] = l[j - gap], l[j]
                else:
                    break

if __name__ == "__main__":
    main(shell_sort)
