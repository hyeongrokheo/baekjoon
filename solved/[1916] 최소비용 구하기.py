"""
problem tier : Gold 5 (solved_old.ac)
"""

import sys
import heapq

INF = 10000000000
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

length = [[INF for j in range(N)] for i in range(N)]

for i in range(M):
    s, e, l = map(lambda x: int(x), sys.stdin.readline().split())
    if length[s-1][e-1] > l:
        length[s-1][e-1] = l

S, E = map(lambda x: int(x), sys.stdin.readline().split())
for i in range(N):
    length[i][i] = 0

dist = [INF for i in range(N)]
dist[S-1] = 0

queue = []
heapq.heappush(queue, (0, S-1))

while len(queue) != 0:
    _, point = heapq.heappop(queue)

    for i in range(N):
        if length[point][i] != INF:
            if dist[i] > dist[point] + length[point][i]:
                dist[i] = dist[point] + length[point][i]
                heapq.heappush(queue, (dist[i], i))

print(dist[E-1])

