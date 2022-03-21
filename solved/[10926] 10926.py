"""
problem tier : Bronze 5 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


def solution():
    inp = input()

    return inp[:-1] + '??!'


print(solution())
