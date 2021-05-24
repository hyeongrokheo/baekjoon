"""
problem tier : Silver 1 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 9999999
N, M = map(lambda x: int(x), sys.stdin.readline().split())

dist = [[INF for j in range(N)] for i in range(N)]
for i in range(M):
    s, e = map(lambda x: int(x), sys.stdin.readline().split())
    dist[s-1][e-1] = 1
    dist[e-1][s-1] = 1
for i in range(N):
    dist[i][i] = 0

for m in range(N):
    for s in range(N):
        for e in range(N):
            if dist[s][e] > dist[s][m] + dist[m][e]:
                dist[s][e] = dist[s][m] + dist[m][e]

min_sum = INF
for i in range(N):
    if min_sum > sum(dist[i]):
        min_sum = sum(dist[i])
        min_num = i+1

print(min_num)
