"""
problem tier : Silver 3 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def solution():
    N = int(input())
    works = []
    for i in range(N):
        works.append(list(map(int, input().split())))

    DP = [[None for i in range(2)] for j in range(15)]

    for w in works:
        T, P = w
        print(T, P)




solution()
