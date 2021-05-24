"""
problem tier : D4 (swexpertacademy.com)
"""

import heapq

INF = 999999999
T = int(input())

for t in range(T):
    N = int(input())
    depth = []
    for i in range(N):
        depth.append(list(map(int, input().strip())))

    dist = [[INF for j in range(N)] for i in range(N)]
    dist[0][0] = 0
    queue = []

    heapq.heappush(queue, (0, [0, 0]))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while len(queue) != 0:
        _, p = heapq.heappop(queue)
        x, y = p[0], p[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] > dist[x][y] + depth[nx][ny]:
                    dist[nx][ny] = dist[x][y] + depth[nx][ny]
                    heapq.heappush(queue, (dist[nx][ny], [nx, ny]))

    print('#{} {}'.format(t+1, dist[N-1][N-1]))
