from random import randrange

from collections import namedtuple

from merge_sort import merge_sort
from quick_sort import quick_sort
from bubble_sort import bubble_sort
from bogo_sort import bogo_sort

COLOUR_DECAY = 0.97

SortConfig = namedtuple("SortConfig", ["algorithm", "max_x", "max_y", "ops_f"])

ops_f = 10

def plot_data():
    loadPixels()
    for x, y in enumerate(data):
        pixels[(height - 1 - y) * width + x] = color(recent[x] * 255, 255, 255)
    updatePixels()

def prep_data(alg_no):
    global data, sorter, recent, ops_f
    config = algs[alg_no]
    data = [randrange(config.max_y) for _ in xrange(config.max_x)]
    sorter = config.algorithm(data)
    recent = [0 for _ in xrange(config.max_x)]
    ops_f = config.ops_f

def setup():
    global algs
    size(1600, 800)
    colorMode(HSB, 255, 255, 255)
    algs = [SortConfig(merge_sort, width, height, 10),
            SortConfig(quick_sort, width, height, 10),
            SortConfig(bubble_sort, width // 2, height // 2, 40),
            SortConfig(bogo_sort, width, height, 10)]
    prep_data(0)

def draw():
    background(0)
    for _ in xrange(ops_f):
        recent[:] = [i * COLOUR_DECAY for i in recent]
        try:
            for op in next(sorter):
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
    elif keyCode == DOWN:
        ops_f //= 2
        if not ops_f:
            ops_f = 1
    print("ops/frame: {}".format(ops_f))