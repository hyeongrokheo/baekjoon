"""
problem tier : Bronze 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


def solution():
    dice = list(map(int, input().split()))
    if len(set(dice)) == 1:
        return 10000 + dice[0] * 1000
    elif len(set(dice)) == 2:
        if dice[0] == dice[1]:
            high = dice[0]
        elif dice[1] == dice[2]:
            high = dice[1]
        else:
            high = dice[0]
        return 1000 + high * 100
    else:
        return max(dice) * 100


print(solution())
