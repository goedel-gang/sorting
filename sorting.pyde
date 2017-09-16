"""
The processing sketch handling visualisation. It's up to the algorithm to
provide some kind of meaningful access hotspot indication - it's not
necessarily very accurate in complexity, but does illustrate the algorithm and
is pretty.
"""

from random import randrange

from collections import namedtuple
from itertools import islice

from quick_sort import quick_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from bitonic_sort import bitonic_sort
from bubble_sort import bubble_sort
from bogo_sort import bogo_sort

COLOUR_DECAY = 0.97

SortConfig = namedtuple("SortConfig", ["algorithm", "max_x", "max_y", "ops_f"])

ops_f = 10

def plot_data():
    loadPixels()
    for x, y in islice(enumerate(data), width):
        pixels[(height - 1 - y) * width + x] = color(recent[x] * 255, 255, 255)
    updatePixels()

def prep_data(alg_no):
    global data, sorter, recent, ops_f
    config = algs[alg_no]
    data = [randrange(config.max_y) for _ in xrange(config.max_x)]
    sorter = config.algorithm(data)
    recent = [0 for _ in xrange(config.max_x)]
    ops_f = config.ops_f
    print()
    print("using {}".format(config.algorithm.func_name))
    print("speed {}".format(ops_f))
    print("array size is {}".format(config.max_x))
    print("max element is {}".format(config.max_y))

def setup():
    global algs
    size(1600, 800)
    colorMode(HSB, 255, 255, 255)
    algs = map(SortConfig, *zip(*[(quick_sort, width, height, 10),
                                  (merge_sort, width, height, 10),
                                  (heap_sort, width, height, 10),
                                  (bitonic_sort, 1024, height, 10),
                                  (bubble_sort, width // 2, height // 2, 40),
                                  (bogo_sort, width, height, 10)]))
    prep_data(0)

def draw():
    background(0)
    for _ in xrange(ops_f):
        recent[:] = [i * COLOUR_DECAY for i in recent]
        try:
            for op in next(sorter):
                if op < width:
                    recent[op] = 1
        except StopIteration:
            pass
    plot_data()

def keyPressed():
    global ops_f
    numv = keyCode - ord('1')
    if 0 <= numv < len(algs):
        prep_data(numv)
    elif keyCode == UP:
        ops_f *= 2
        print("ops/frame: {}".format(ops_f))
    elif keyCode == DOWN:
        ops_f //= 2
        if not ops_f:
            ops_f = 1
        print("ops/frame: {}".format(ops_f))