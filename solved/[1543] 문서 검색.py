"""
problem tier : Silver 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def solution():
    count = 0
    S = input().strip()
    W = input().strip()
    while S.find(W) != -1:
        S = S[S.find(W)+len(W):]
        # print(S)
        count += 1
    return count


print(solution())
