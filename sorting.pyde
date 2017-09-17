"""
The processing sketch handling visualisation. It's up to the algorithm to
provide some kind of meaningful access hotspot indication - it's not
necessarily very accurate in complexity, but does illustrate the algorithm and
is pretty. The more "serious" algorithms are number keys, the rest are qw...
"""

from random import randrange

from collections import namedtuple

from quick_sort import quick_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from bitonic_sort import bitonic_sort
from shell_sort import shell_sort
from lsd_radix_sort import lsd_radix_sort
from counting_sort import counting_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bogo_sort import bogo_sort

COLOUR_DECAY = 0.97

SortConfig = namedtuple("SortConfig", ["algorithm", "max_x", "max_y", "ops_f"])

ops_f = 10

def plot_data():
    loadPixels()
    for x, y in enumerate(data):
        pixels[(height - 1 - y) * width + x] = color(recent[x] * 255, 255, 255)
    updatePixels()

def prep_data(config):
    global data, sorter, recent, ops_f
    data = [randrange(config.max_y) for _ in xrange(config.max_x)]
    sorter = config.algorithm(data)
    recent = [0 for _ in xrange(config.max_x)]
    ops_f = config.ops_f
    print
    print("using {}".format(config.algorithm.func_name))
    print("speed {}".format(ops_f))
    print("array size is {}".format(config.max_x))
    print("max element is {}".format(config.max_y))

def setup():
    global alg_map
    size(1600, 800)
    colorMode(HSB, 255, 255, 255)
    algs = map(SortConfig, *zip(*[(quick_sort, width, height, 10),
                                  (merge_sort, width, height, 10),
                                  (heap_sort, width, height, 10),
                                  (bitonic_sort, 1024, height, 10),
                                  (shell_sort, width, height, 10),
                                  (lsd_radix_sort, width, height, 10),
                                  (counting_sort, width, height, 10),
                                  (bubble_sort, width // 2, height // 2, 40),
                                  (selection_sort, width // 2, height // 2, 40),
                                  (insertion_sort, width // 2, height // 2, 40),
                                  (bogo_sort, width, height, 10)]))
    alg_map = dict(zip("1234567qwert", algs))
    prep_data(algs[0])

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
    if key in alg_map:
        prep_data(alg_map[key])
    elif keyCode == UP:
        ops_f *= 2
        print("ops/frame: {}".format(ops_f))
    elif keyCode == DOWN:
        ops_f //= 2
        if not ops_f:
            ops_f = 1
        print("ops/frame: {}".format(ops_f))