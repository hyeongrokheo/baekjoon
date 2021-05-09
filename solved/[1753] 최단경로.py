"""
problem tier : Gold 5 (solved_old.ac)
"""

import sys
import heapq

INF = 99999999
V, E = map(lambda x: int(x), input().split())
K = int(input())

Edges = {}
for i in range(E):
    u, v, w = map(lambda x: int(x), sys.stdin.readline().split())
    if u not in Edges.keys():
        Edges[u] = {}
    if v in Edges[u].keys():
        Edges[u][v] = min(Edges[u][v], w)
    else:
        Edges[u][v] = w

finished = [False] * (V+1)
distance = [INF] * (V+1)
distance[K] = 0
pri_queue = []
heapq.heappush(pri_queue, (0, K))


while True:
    if len(pri_queue) == 0:
        break
    v = heapq.heappop(pri_queue)[1]

    if finished[v]:
        continue
    if v not in Edges.keys():
        finished[v] = True
        continue

    for adj in Edges[v].keys():
        distance[adj] = min(distance[adj], distance[v] + Edges[v][adj])
        heapq.heappush(pri_queue, (distance[adj], adj))
    finished[v] = True

distance = list(map(lambda x: 'INF' if x == INF else x, distance))[1:]

for d in distance:
    print(d)