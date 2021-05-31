"""
problem tier : Gold 4 (solved.ac)
"""

from collections import deque
import sys

INF = 9999999
N, M = map(int, sys.stdin.readline().split())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

dist = [[[INF, INF] for j in range(M)] for i in range(N)]

dist[0][0] = [0, 0]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append((0, 0, 0))
while len(queue) > 0:
    x, y, z = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if z == 0:
                if arr[nx][ny] == 0:
                    if dist[nx][ny][0] > dist[x][y][z] + 1:
                        dist[nx][ny][0] = dist[x][y][z] + 1
                        queue.append((nx, ny, 0))
                else:
                    if dist[nx][ny][1] > dist[x][y][z] + 1:
                        dist[nx][ny][1] = dist[x][y][z] + 1
                        queue.append((nx, ny, 1))
            else:
                if arr[nx][ny] == 0:
                    if dist[nx][ny][1] > dist[x][y][z] + 1:
                        dist[nx][ny][1] = dist[x][y][z] + 1
                        queue.append((nx, ny, 1))

result = min(dist[N-1][M-1])
if result == INF:
    print(-1)
else:
    print(result + 1)
