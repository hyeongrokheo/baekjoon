"""
problem tier : Gold 2 (solved.ac)
"""

import heapq
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

maps = []
for i in range(N):
    maps.append(list(input().strip()))

for m in maps:
    print(m)

bfs = []
