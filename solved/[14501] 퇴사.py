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

    works.reverse()

    DP = [0]
    for work in works:
        T, P = work
        if len(DP) < T:
            DP.append(DP[-1])
        else:
            DP.append(max(DP[-1], DP[-T] + P))

    print(max(DP))

solution()
