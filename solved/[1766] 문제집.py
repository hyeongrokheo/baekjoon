"""
problem tier : Gold 2 (solved.ac)
"""

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

prob = [[0, []] for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    prob[B][0] += 1
    prob[A][1].append(B)

Q = []
for i in range(1, N+1):
    if prob[i][0] == 0:
        heapq.heappush(Q, i)

result = []
while len(Q) > 0:
    pn = heapq.heappop(Q)
    result.append(pn)

    for next in prob[pn][1]:
        prob[next][0] -= 1
        if prob[next][0] == 0:
            heapq.heappush(Q, next)

print(' '.join(map(str, result)))
