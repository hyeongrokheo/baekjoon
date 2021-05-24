"""
problem tier : Gold 3 (solved.ac)
"""

import heapq

INF = 9999999999
N, M, X = map(int, input().split())

length = [[INF for j in range(N)] for i in range(N)]
length_rev = [[INF for j in range(N)] for i in range(N)]

for i in range(N):
    length[i][i] = 0
    length_rev[i][i] = 0

for i in range(M):
    s, e, d = map(int, input().split())
    length[s-1][e-1] = d
    length_rev[e-1][s-1] = d

queue = []
heapq.heappush(queue, (0, X-1))
dist = [INF for i in range(N)]
dist[X-1] = 0

while len(queue) != 0:
    _, p = heapq.heappop(queue)
    for i in range(N):
        if dist[i] > dist[p] + length[p][i]:
            dist[i] = dist[p] + length[p][i]
            heapq.heappush(queue, (dist[i], i))

queue = []
heapq.heappush(queue, (0, X-1))
dist2 = [INF for i in range(N)]
dist2[X-1] = 0

while len(queue) != 0:
    _, p = heapq.heappop(queue)
    for i in range(N):
        if dist2[i] > dist2[p] + length_rev[p][i]:
            dist2[i] = dist2[p] + length_rev[p][i]
            heapq.heappush(queue, (dist2[i], i))

dist_sum = []
for i in range(N):
    dist_sum.append(dist[i] + dist2[i])
print(max(dist_sum))

