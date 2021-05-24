"""
problem tier : Gold 4 (solved.ac)
"""

import heapq
import sys

INF = 999999999
N, E = map(lambda x: int(x), sys.stdin.readline().split())
length = [[INF for j in range(N)] for i in range(N)]

for i in range(N):
    length[i][i] = 0

for i in range(E):
    a, b, c = map(lambda x: int(x), sys.stdin.readline().split())
    length[a-1][b-1] = c
    length[b-1][a-1] = c

v1, v2 = map(lambda x: int(x), sys.stdin.readline().split())

dists = [[INF for j in range(N)] for i in range(3)]
starts = [0, v1-1, v2-1]
for i in range(3):
    dists[i][starts[i]] = 0

for i in range(3):
    dist = dists[i]
    queue = []

    heapq.heappush(queue, (0, starts[i]))

    while len(queue) != 0:
        _, p = heapq.heappop(queue)
        for i in range(N):
            if dist[i] > dist[p] + length[p][i]:
                dist[i] = dist[p] + length[p][i]
                heapq.heappush(queue, (dist[i], i))

result = min(dists[0][v1-1] + dists[1][v2-1] + dists[2][N-1], dists[0][v2-1] + dists[2][v1-1] + dists[1][N-1])
if result >= INF:
    print(-1)
else:
    print(result)
