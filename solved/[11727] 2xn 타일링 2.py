"""
problem tier : Silver 3 (solved.ac)
"""

import sys
sys.setrecursionlimit(10**8)

n = int(input())
memo = [None for i in range(n+1)]

memo[1] = 1
if n > 1:
    memo[2] = 3

def tile(n):
    if not memo[n]:
        memo[n] = (tile(n-1) + tile(n-2)*2) % 10007

    return memo[n]

print(tile(n))
