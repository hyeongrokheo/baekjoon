"""
problem tier : Gold 5 (solved_old.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 99999
N = int(input())
dist = [[INF for j in range(N)] for i in range(N)]
for i in range(N):
    dist[i][i] = 0
while True:
    s, e = map(lambda x: int(x), sys.stdin.readline().split())
    if s == -1 and e == -1:
        break
    dist[s-1][e-1] = 1
    dist[e-1][s-1] = 1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if dist[s][e] > dist[s][m] + dist[m][e]:
                dist[s][e] = dist[s][m] + dist[m][e]

min_score = INF
cand = []
for i in range(N):
    score = max(dist[i])
    if min_score > score:
        min_score = score
        cand = [i+1]
    elif min_score == score:
        cand.append(i+1)

print(min_score, len(cand))
print(' '.join(map(lambda x: str(x), cand)))
