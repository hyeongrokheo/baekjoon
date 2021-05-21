"""
problem tier : Gold 4 (solved_old.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 9999999999
N, M, R = map(lambda x: int(x), sys.stdin.readline().split())
item = list(map(lambda x: int(x), sys.stdin.readline().split()))
dist = [[INF for j in range(N)] for i in range(N)]

for i in range(R):
    s, e, d = map(lambda x: int(x), sys.stdin.readline().split())
    if dist[s-1][e-1] > d:
        dist[s-1][e-1] = d
    if dist[e-1][s-1] > d:
        dist[e-1][s-1] = d

for i in range(N):
    dist[i][i] = 0

for m in range(N):
    for s in range(N):
        for e in range(N):
            if dist[s][e] > dist[s][m] + dist[m][e]:
                dist[s][e] = dist[s][m] + dist[m][e]

# for d in dist:
#     print(d)

max_value = 0
for i in range(N):
    adj = dist[i]
    item_value = 0
    for j in range(N):
        if adj[j] <= M:
            item_value += item[j]
    if max_value < item_value:
        max_value = item_value

print(max_value)
