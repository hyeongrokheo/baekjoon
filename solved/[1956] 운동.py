"""
problem tier : Gold 4 (solved.ac)
pypy3
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 99999999
V, E = map(lambda x: int(x), sys.stdin.readline().split())

dist = [[INF for j in range(V)] for i in range(V)]
for i in range(E):
    s, e, d = map(lambda x: int(x), sys.stdin.readline().split())
    dist[s-1][e-1] = d

for m in range(V):
    for s in range(V):
        for e in range(V):
            if dist[s][e] > dist[s][m] + dist[m][e]:
                dist[s][e] = dist[s][m] + dist[m][e]

min_dist = INF
for i in range(V):
    if min_dist > dist[i][i]:
        min_dist = dist[i][i]

if min_dist == INF:
    print(-1)
else:
    print(min_dist)

