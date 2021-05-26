"""
problem tier : Platinum 5 (solved.ac)
pypy3
"""

import heapq
import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 2000000000
N, M, K = map(int, sys.stdin.readline().split())

length = {}
dist = [[] for i in range(N+1)]
heapq.heappush(dist[1], (0, 0))

for i in range(M):
    s, e, d = map(int, sys.stdin.readline().split())
    if s in length.keys():
        if e in length[s].keys():
            if length[s][e] > d:
                length[s][e] = d
        else:
            length[s][e] = d
    else:
        length[s] = {}
        length[s][e] = d
queue = []
heapq.heappush(queue, (0, 1))

while len(queue) != 0:
    d, p = heapq.heappop(queue)

    if p in length.keys():
        adj = length[p]
    else:
        adj = {}

    for adj_p in adj.keys():
        adj_p_dist = dist[adj_p]
        len_1_to_adj_p = adj[adj_p] + d
        if len(adj_p_dist) < K:
            heapq.heappush(adj_p_dist, (-len_1_to_adj_p, len_1_to_adj_p))
            heapq.heappush(queue, (len_1_to_adj_p, adj_p))
        else:
            X = heapq.heappop(adj_p_dist)
            if X[1] > len_1_to_adj_p:
                heapq.heappush(adj_p_dist, (-len_1_to_adj_p, len_1_to_adj_p))
                heapq.heappush(queue, (len_1_to_adj_p, adj_p))
            else:
                heapq.heappush(adj_p_dist, X)

for d in dist[1:]:
    if len(d) < K:
        print(-1)
    else:
        print(d[0][1])
