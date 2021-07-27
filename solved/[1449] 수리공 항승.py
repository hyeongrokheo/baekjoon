"""
problem tier : Silver 3 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def solution():
    N, L = map(int, input().split())
    M = list(map(int, input().split()))
    M.sort()

    flag = 0
    count = 0
    for m in M:
        if m > flag:
            flag = m+L-1
            count += 1

    return count


print(solution())