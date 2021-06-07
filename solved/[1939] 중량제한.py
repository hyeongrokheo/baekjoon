"""
problem tier : Gold 4 (solved.ac)
"""

import heapq
import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

maps = [{} for i in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    if b not in maps[a].keys():
        maps[a][b] = c
    else:
        maps[a][b] = max(maps[a][b], c)

    if a not in maps[b].keys():
        maps[b][a] = c
    else:
        maps[b][a] = max(maps[b][a], c)

weights = [0 for i in range(N+1)]

S, E = map(int, input().split())
weights[S] = 2000000000

Q = []
heapq.heappush(Q, (0, S))

while len(Q) > 0:
    _, p = heapq.heappop(Q)
    if weights[p] < weights[E]:
        break
    if p == E:
        break
    for next in maps[p].keys():
        if weights[next] < min(weights[p], maps[p][next]):
            weights[next] = min(weights[p], maps[p][next])
            heapq.heappush(Q, (-weights[next], next))

print(weights[E])
