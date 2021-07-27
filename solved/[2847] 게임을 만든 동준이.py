"""
problem tier : Silver 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def solution():
    N = int(input())
    S = []
    for i in range(N):
        S.append(int(input()))
    S.reverse()
    # print(S)
    score = 20001
    count = 0
    for s in S:
        if s >= score:
            count += s - score + 1
            s = score-1
        score = s
    return count


print(solution())
