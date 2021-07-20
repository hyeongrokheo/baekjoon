"""
problem tier : Platinum 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

M = int(input())
P = list(map(int, input().split()))

result = 0
for p in P:
    result ^= p

if result == 0:
    print('cubelover')
else:
    print('koosaga')
