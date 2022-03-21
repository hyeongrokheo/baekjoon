"""
problem tier : Platinum 3 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

result = 0

for i in arr:
    result = result ^ i

if result == 1:
    print('cubelover')
else:
    print('koosaga')
