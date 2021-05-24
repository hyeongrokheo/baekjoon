"""
problem tier : Gold 4 (solved.ac)
"""

import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

INF = 999999
T = 0
while True:
    T += 1
    N = int(input())
    if N == 0:
        break

    maps = []
    for i in range(N):
        maps.append(list(map(int, input().split())))

    dijk = [[INF for j in range(N)] for i in range(N)]
    dijk[0][0] = maps[0][0]

    queue = []
    heapq.heappush(queue, (dijk[0][0], [0, 0]))

    while len(queue) != 0:
        _, p = heapq.heappop(queue)
        x, y = p[0], p[1]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if dijk[nx][ny] > dijk[x][y] + maps[nx][ny]:
                    dijk[nx][ny] = dijk[x][y] + maps[nx][ny]
                    heapq.heappush(queue, (dijk[nx][ny], [nx, ny]))

    print('Problem {}: {}'.format(T, dijk[N-1][N-1]))
