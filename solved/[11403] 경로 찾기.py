"""
problem tier : Silver 1 (solved_old.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 999999
N = int(input())

dist = []
for i in range(N):
    dist.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if dist[i][j] == 0:
            dist[i][j] = INF

for m in range(N):
    for s in range(N):
        for e in range(N):
            if dist[s][e] > dist[s][m] + dist[m][e]:
                dist[s][e] = 1

for i in range(N):
    for j in range(N):
        if dist[i][j] == INF:
            dist[i][j] = 0

for d in dist:
    print(' '.join(map(lambda x: str(x), d)))
