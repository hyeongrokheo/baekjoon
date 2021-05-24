"""
problem tier : Gold 3 (solved_old.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

INF = 999999999
N = int(input())
M = int(input())

dist = [[None for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        dist[i][j] = [INF, []]

for i in range(M):
    s, e, d = map(lambda x: int(x), sys.stdin.readline().split())
    if dist[s-1][e-1][0] > d:
        dist[s-1][e-1][0] = d
    # dist[e-1][s-1][0] = d

# for d in dist:
#     print(d)
# print()
for i in range(N):
    dist[i][i][0] = 0

for m in range(N):
    for s in range(N):
        for e in range(N):
            if dist[s][e][0] > dist[s][m][0] + dist[m][e][0]:
                dist[s][e][0] = dist[s][m][0] + dist[m][e][0]
                dist[s][e][1] = dist[s][m][1].extend(dist[m][e][1])

for d in dist:
    print(' '.join(map(lambda x: str(x[0]), d)))

for d in dist:
    print(d)
for i in range(N):
    for j in range(N):
        if dist[i][j][0] == 0 or dist[i][j][0] == INF:
            print(0)
        elif len(dist[i][j][1]) == 0:
            print(2, i+1, j+1)
        else:
            print(len(dist[i][j][1])+2, i+1, ' '.join(map(lambda x: str(x+1), dist[i][j][1])), j+1)
