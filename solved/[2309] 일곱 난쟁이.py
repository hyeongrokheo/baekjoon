"""
problem tier : Bronze 2 (solved.ac)
"""

import itertools
import sys
# sys.stdin = open('./input.txt', 'r')

input = sys.stdin.readline


def solution():
    arr = []
    for i in range(9):
        arr.append(int(input()))

    comb = itertools.combinations(arr, 7)

    for c in comb:
        if sum(c) == 100:
            result = list(c)
            result.sort()
            for r in result:
                print(r)
            return


solution()
