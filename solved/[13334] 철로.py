"""
problem tier : Gold 2 (solved.ac)
"""

import heapq
import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())

points = []
for i in range(N):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    points.append([h, o])

D = int(input())

points.sort(key=lambda x: x[1])

Q = []
count = 0
for p in points:
    heapq.heappush(Q, p[0])
    while len(Q) > 0 and Q[0] < p[1] - D:
        heapq.heappop(Q)

    count = max(count, len(Q))

print(count)


