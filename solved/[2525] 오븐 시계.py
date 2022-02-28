"""
problem tier : Bronze 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


def solution():
    A, B = map(int, input().split())
    C = int(input())
    B += C
    if B >= 60:
        A += B // 60
        B = B % 60
    if A >= 24:
        A = A % 24
    return '{} {}'.format(A, B)


print(solution())
