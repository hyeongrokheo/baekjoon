"""
problem tier : Gold 4 (solved.ac)
"""

import heapq
import sys

INF = 9999999
N, M = map(int, sys.stdin.readline().split())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

dist_from_S = [[INF for j in range(M)] for i in range(N)]
dist_from_E = [[INF for j in range(M)] for i in range(N)]

dist_from_S[0][0] = 0
dist_from_E[N-1][M-1] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = []
heapq.heappush(queue, (0, 0))
while len(queue) > 0:
    x, y = heapq.heappop(queue)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if dist_from_S[nx][ny] > dist_from_S[x][y] + 1:
                dist_from_S[nx][ny] = dist_from_S[x][y] + 1
                if arr[nx][ny] == 0:
                    heapq.heappush(queue, (nx, ny))

queue = []
heapq.heappush(queue, (N-1, M-1))
while len(queue) > 0:
    x, y = heapq.heappop(queue)
    print(x, y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if dist_from_E[nx][ny] > dist_from_E[x][y] + 1:
                dist_from_E[nx][ny] = dist_from_E[x][y] + 1
                if arr[nx][ny] == 0:
                    heapq.heappush(queue, (nx, ny))

min_distance = INF
for i in range(N):
    for j in range(M):
        if dist_from_S[i][j] + dist_from_E[i][j] < INF:
            distance = dist_from_S[i][j] + dist_from_E[i][j] + 1
            if min_distance > distance:
                min_distance = distance

if min_distance == INF:
    print(-1)
else:
    print(min_distance)
