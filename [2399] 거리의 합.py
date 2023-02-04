"""
problem tier : Bronze 2 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')


def solution():
    N = int(input())
    positions = list(map(int, input().split()))
    sum_distance = 0

    for position_1 in positions:
        for position_2 in positions:
            sum_distance += abs(position_1 - position_2)

    print(sum_distance)


solution()
