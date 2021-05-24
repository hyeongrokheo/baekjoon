"""
problem tier : Gold 4 (solved_old.ac)
"""

import heapq
import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 99999
M, N = map(lambda x: int(x), sys.stdin.readline().split())

maps = []
for i in range(N):
    maps.append(list(map(lambda x: 1 if x == '1' else 0, sys.stdin.readline().strip())))

# print(maps)

dijk = [[INF for j in range(M)] for i in range(N)]
dijk[0][0] = 0
queue = []
heapq.heappush(queue, (0, [0, 0]))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while len(queue) != 0:
    _, point = heapq.heappop(queue)

    for i in range(4):
        x = point[0] + dx[i]
        y = point[1] + dy[i]
        # print(x, y)
        if 0 <= x < N and 0 <= y < M:
            if dijk[x][y] > dijk[point[0]][point[1]] + maps[x][y]:
                dijk[x][y] = dijk[point[0]][point[1]] + maps[x][y]
                heapq.heappush(queue, (dijk[x][y], [x, y]))

# for d in dijk:
#     print(d)

print(dijk[N-1][M-1])


