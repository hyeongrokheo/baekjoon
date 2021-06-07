"""
problem tier : Gold 4 (solved.ac)
"""

from collections import deque
import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

maps = [{} for i in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    # if b not in maps[a].keys():
    #     maps[a]
    if b not in maps[a].keys():
        maps[a][b] = c
    else:
        maps[a][b] = max(maps[a][b], c)

    if a not in maps[b].keys():
        maps[b][a] = c
    else:
        maps[b][a] = max(maps[b][a], c)

dist = [0 for i in range(N+1)]

S, E = map(int, input().split())
dist[S] = 0

Q = deque()
Q.append(S)

while len(Q) > 0:
    p = Q.popleft()
    for next in maps[p].keys():


print(maps)

