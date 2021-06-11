"""
problem tier : Gold 4 (solved.ac)
"""

import heapq
import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())
days = [[] for i in range(10000)]

for i in range(N):
    p, d = map(int, input().split())
    days[d-1].append(p)
days.reverse()

Q = []
money = 0
for d in days:
    for p in d:
        heapq.heappush(Q, (-p, p))
    if len(Q) > 0:
        _, p = heapq.heappop(Q)
        money += p

print(money)
