"""
problem tier : Gold 5 (solved_old.ac)
"""

import sys

INF = 99999999
V, E = map(lambda x: int(x), input().split())

K = int(input())

Edges = {}

for i in range(E):
    u, v, w = map(lambda x: int(x), sys.stdin.readline().split())
    if not u in Edges.keys():
        Edges[u] = {}
    Edges[u][v] = w
print(Edges)
