"""
problem tier : Gold 3 (solved.ac)
"""

from copy import deepcopy
import heapq
import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 999999999
N = int(input())
M = int(input())

length = {}

for i in range(M):
    s, e, l = map(int, sys.stdin.readline().split())
    if s not in length.keys():
        length[s] = {}
    if e not in length[s].keys():
        length[s][e] = l
    else:
        if length[s][e] > l:
            length[s][e] = l

S, E = map(int, input().split())

dist = [INF for i in range(N+1)]
dist[S] = 0
path = [[] for i in range(N+1)]

queue = []
heapq.heappush(queue, (0, S))

while len(queue) != 0:
    _, p = heapq.heappop(queue)

    if p in length.keys():
        for q in length[p].keys():
            if dist[q] > dist[p] + length[p][q]:
                dist[q] = dist[p] + length[p][q]
                path[q] = deepcopy(path[p])
                path[q].extend([p])
                heapq.heappush(queue, (dist[q], q))

print(dist[E])
print(len(path[E]) + 1)
print(' '.join(map(str, path[E])), E)
