"""
problem tier : Silver 3 (solved.ac)
"""

import sys
import itertools
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


def solution():
    N = int(input())
    for per in itertools.permutations([i+1 for i in range(N)], N):
        print(' '.join(list(map(str, per))))


solution()
