# vim: ft=python

"""
The processing sketch handling visualisation. It's up to the algorithm to
provide some kind of meaningful access hotspot indication - it's not
necessarily very accurate in complexity, but does illustrate the algorithm and
is pretty. The more "serious" algorithms are number keys, the rest are qwer
"""

from random import randrange
from time import sleep
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

COLOUR_DECAY = 0.99

# Used for video creation
CYCLE = True
SAVE_FRAMES = False

TL_SIZE = 30

SortConfig = namedtuple(
    "SortConfig", ["algorithm", "max_x", "max_y", "ops_f", "minw", "maxw"])

ops_f = 10

def plot_data():
    data_len = len(data)
    data_height = max(data)
    for x, y in enumerate(data):
        x_val = map(x, 0, data_len, 0, width)
        y_val = map(y, 0, data_height, 0, height)
        fill(recent[x] * 255, 255, 255)
        ellipse(x_val, height - y_val, *[map(recent[x], 0, 1, minw, maxw)] * 2)

def prep_data(config):
    global data, sorter, recent, ops_f, minw, maxw, tl_text, tl_shade, cycle_buffer
    cycle_buffer = 3000
    data = [randrange(config.max_y) for _ in xrange(config.max_x)]
    sorter = config.algorithm(data)
    recent = [0 for _ in xrange(config.max_x)]
    ops_f = config.ops_f
    minw = config.minw
    maxw = config.maxw
    print
    print("using {}".format(config.algorithm.func_name))
    print("speed {}".format(ops_f))
    print("array size is {}".format(config.max_x))
    print("max element is {}".format(config.max_y))
    tl_text = config.algorithm.func_name
    tl_shade = 1

def setup():
    global alg_map, algs, cycle_index, f
    size(1280, 720)
    f = createFont("courier", TL_SIZE, True)
    textFont(f, TL_SIZE)
    cycle_index = 0
    noStroke()
    colorMode(HSB, 255, 255, 255)
    algs = map(SortConfig, *zip(*[(quick_sort, 1024, height, 10, 2, 10),
                                  (merge_sort, 1024, height, 10, 2, 10),
                                  (heap_sort, 1024, height, 10, 2, 10),
                                  (bitonic_sort, 1024, height, 10, 2, 10),
                                  (shell_sort, 1024, height, 10, 2, 10),
                                  (lsd_radix_sort, 1024, height, 10, 2, 10),
                                  (counting_sort, 1024, height, 10, 2, 10),
                                  (bubble_sort, 200, height, 10, 10, 30),
                                  (selection_sort, 200, height, 10, 10, 30),
                                  (insertion_sort, 200, height, 10, 10, 30),
                                  (bogo_sort, width, height, 10, 2, 10)]))
    alg_map = dict(zip("1234567qwert", algs))
    prep_data(algs[cycle_index])

def draw():
    global cycle_index, tl_shade, cycle_buffer
    background(0)
    fill(tl_shade * 255)
    tl_shade *= COLOUR_DECAY
    text(tl_text, 50, 50)
    for _ in xrange(ops_f):
        recent[:] = [i * COLOUR_DECAY for i in recent]
        try:
            for op in next(sorter):
                if op < width:
                    recent[op] = 1
        except StopIteration:
            if CYCLE:
                if cycle_buffer < 0:
                    cycle_index += 1
                    prep_data(algs[cycle_index])
                else:
                    cycle_buffer -= 1
    plot_data()
    if SAVE_FRAMES:
        saveFrame("data/sort_vid-######.png")

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
