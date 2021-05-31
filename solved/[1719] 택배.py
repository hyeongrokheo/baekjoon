"""
problem tier : Gold 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

INF = 99999999
N, M = map(int, input().split())

dist = [[INF for j in range(N)] for i in range(N)]
for i in range(N):
    dist[i][i] = 0
via = [['-' for j in range(N)] for i in range(N)]

for i in range(M):
    s, e, d = map(int, input().split())
    dist[s-1][e-1] = d
    dist[e-1][s-1] = d
    via[s-1][e-1] = e
    via[e-1][s-1] = s

for m in range(N):
    for s in range(N):
        for e in range(N):
            if dist[s][e] > dist[s][m] + dist[m][e]:
                # print(s, e, m, dist[s][m] + dist[m][e])
                dist[s][e] = dist[s][m] + dist[m][e]
                via[s][e] = via[s][m]

for v in via:
    print(' '.join(map(str, v)))
