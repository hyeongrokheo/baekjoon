"""
problem tier : Silver 2 (solved.ac)
"""

import itertools
import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


def solution():
    N = int(input())
    A = list(map(int, input().split()))

    AS = list(itertools.permutations(A, N))

    max_result = 0
    for a in AS:
        result = 0
        for i in range(len(a) - 1):
            result += abs(a[i] - a[i + 1])
        if max_result < result:
            max_result = result

    # print(max_result)
    return max_result

print(solution())
