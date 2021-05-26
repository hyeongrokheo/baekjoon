"""
problem tier : Gold 4 (solved.ac)
"""

import heapq
# import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 99999
N = int(input())

maps = []
dist = [[INF for j in range(N)] for i in range(N)]
dist[0][0] = 0
for i in range(N):
    maps.append(list(map(lambda x: 0 if x == '1' else 1, input().strip())))

queue = []
heapq.heappush(queue, (0, [0, 0]))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while len(queue) != 0:
    _, p = heapq.heappop(queue)
    x, y = p[0], p[1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if dist[nx][ny] > dist[x][y] + maps[nx][ny]:
                dist[nx][ny] = dist[x][y] + maps[nx][ny]
                heapq.heappush(queue, (dist[nx][ny], [nx, ny]))

print(dist[N-1][N-1])
