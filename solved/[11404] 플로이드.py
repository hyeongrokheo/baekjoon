"""
problem tier : Gold 4 (solved.ac)
"""

import sys
# sys.stdin = open('./../input.txt', 'r')
# input = sys.stdin.readline

INF = 9999999
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dist = [[INF for j in range(n)] for i in range(n)]
for i in range(n):
    dist[i][i] = 0

for i in range(m):
    s, e, d = map(lambda x: int(x), sys.stdin.readline().strip().split())
    if dist[s-1][e-1] > d:
        dist[s-1][e-1] = d
for m in range(n):
    for s in range(n):
        for e in range(n):
            if dist[s][e] > dist[s][m] + dist[m][e]:
                dist[s][e] = dist[s][m] + dist[m][e]

for d in dist:
    print(' '.join(map(lambda x: str(x) if x != INF else '0', d)))

