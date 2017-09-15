import random

from merge_sort import merge_sort
from quick_sort import quick_sort

algs = [merge_sort, quick_sort]

ops_f = 10

def plot_data():
    loadPixels()
    for x, y in enumerate(data):
        pixels[(height - 1 - y) * width + x] = color(255)
    updatePixels()

def prep_data(alg_no):
    global data, sorter
    data = [random.randrange(height) for _ in xrange(width)]
    sorter = algs[alg_no](data)

def setup():
    size(1600, 800)
    prep_data(0)

def draw():
    background(0)
    for _ in xrange(ops_f):
        try:
            next(sorter)
        except StopIteration:
            break
    plot_data()

def keyPressed():
    global ops_f
    print("ops/frame: {}".format(ops_f))
    numv = keyCode - ord('1')
    if 0 <= numv < len(algs):
        prep_data(numv)
    elif keyCode == UP:
        ops_f *= 2
    elif keyCode == DOWN:
        ops_f //= 2
        if not ops_f:
            ops_f = 1