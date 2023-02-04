"""
problem tier : Silver 2 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')


def solution():
    N = int(input())
    scores = list(map(int, input().split()))

    for i, score in enumerate(scores):
        print(i + 1 - score)


solution()
