"""
problem tier : Gold 5 (solved.ac)
"""

import heapq

INF = 1000000
N, K = map(int, input().split())

dist = [INF for i in range(100001)]
dist[N] = 0

queue = []
heapq.heappush(queue, (0, N))

while len(queue) != 0:
    _, p = heapq.heappop(queue)
    if p > 0:
        if dist[p-1] > dist[p] + 1:
            dist[p-1] = dist[p] + 1
            heapq.heappush(queue, (dist[p-1], p-1))
    if p < 100000:
        if dist[p+1] > dist[p] + 1:
            dist[p+1] = dist[p] + 1
            heapq.heappush(queue, (dist[p+1], p+1))
    if 0 < p <= 50000:
        if dist[p*2] > dist[p]:
            dist[p*2] = dist[p]
            heapq.heappush(queue, (dist[p*2], p*2))

print(dist[K])


