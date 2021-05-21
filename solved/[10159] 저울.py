"""
problem tier : Gold 3 (solved_old.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
M = int(input())

INF = 99999999
heavy = [[INF for j in range(N)] for i in range(N)]
light = [[INF for j in range(N)] for i in range(N)]

for i in range(N):
    heavy[i][i] = 0
    light[i][i] = 0

for i in range(M):
    h, l = map(lambda x: int(x), sys.stdin.readline().split())
    heavy[h-1][l-1] = 1
    light[l-1][h-1] = 1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if heavy[s][e] > heavy[s][m] + heavy[m][e]:
                heavy[s][e] = heavy[s][m] + heavy[m][e]
            if light[s][e] > light[s][m] + light[m][e]:
                light[s][e] = light[s][m] + light[m][e]

for s in range(N):
    unknown = 0
    for e in range(N):
        if heavy[s][e] == INF and light[s][e] == INF:
            unknown += 1
    print(unknown)
