"""
problem tier : Gold 1 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


def solution():
    N, K = map(int, input())
    arr = list(map(int, input().split()))

    socket = [None] * N



print(solution())
