"""
problem tier : Gold 4 (solved_old.ac)
pypy3
"""

import sys

INF = 999999
N, M = map(lambda x: int(x), sys.stdin.readline().split())

up = [[INF for j in range(N)] for i in range(N)]
down = [[INF for j in range(N)] for i in range(N)]

for i in range(M):
    s, b = map(lambda x: int(x), sys.stdin.readline().split())
    up[b-1][s-1] = 1
    down[s-1][b-1] = 1

for i in range(N):
    up[i][i] = 1
    down[i][i] = 1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if up[s][e] > up[s][m] + up[m][e]:
                up[s][e] = 1
            if down[s][e] > down[s][m] + down[m][e]:
                down[s][e] = 1


count = 0
for i in range(N):
    can_measure = True
    for j in range(N):
        if up[i][j] == INF and down[i][j] == INF:
            can_measure = False
            break

    if can_measure:
        count += 1

print(count)
