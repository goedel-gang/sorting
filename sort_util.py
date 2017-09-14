"""
Utility functions for other command-line sorting scripts
"""

import argparse
import random

def get_args():
    parser = argparse.ArgumentParser(description="A sorting program")
    parser.add_argument("-l", "--length", type=int, default=10,
                        help="length of list to generate/sort")
    parser.add_argument("-r", "--range", type=int, default=100,
                        help="range of random integers to generate")
    parser.add_argument("-p", "--print", action="store_true",
                        help="print lists (by default only correctness is printed")
    return parser.parse_args()

def randlist(args):
    ret = [random.randrange(args.range) for _ in range(args.length)]
    return ret

def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True
