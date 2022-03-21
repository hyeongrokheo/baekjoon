"""
problem tier : Diamond 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def rook(x, y):
    return x ^ y


def bishop(x, y):
    return min(x, y)


def king(x, y):
    return


def night(x, y):
    return


def palace(x, y):
    return