"""
problem tier : Silver 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def solution():
    S = list(map(lambda x: True if x == '1' else False, input()))
    standard = S[0]
    flipping = False
    count = 0
    for s in S:
        if s == standard:
            if flipping:
                flipping = not flipping
            else:
                continue
        else:
            if flipping:
                continue
            else:
                flipping = not flipping
                count += 1
    return count


print(solution())
