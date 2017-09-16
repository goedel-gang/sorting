from random import randrange

from sort_util import *

def shuffle(x):
    for i in reversed(range(1, len(x))):
        j = randrange(i + 1)
        x[i], x[j] = x[j], x[i]

def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def bogo_sort(l):
    while not is_sorted(l):
        shuffle(l)

if __name__ == "__main__":
    main(bogo_sort)
