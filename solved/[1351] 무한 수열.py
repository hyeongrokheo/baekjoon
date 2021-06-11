"""
problem tier : Gold 4 (solved.ac)
"""

import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, P, Q = map(int, input().split())

memo = {}
memo[0] = 1


def A(n):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = A(n//P) + A(n//Q)
        return memo[n]

print(A(N))
