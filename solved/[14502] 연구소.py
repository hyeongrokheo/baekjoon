"""
problem tier : Gold 5 (solved_old.ac)
"""

from copy import deepcopy
from collections import deque

N, M = map(lambda x: int(x), input().split())

original_labs = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_safety = 0

for i in range(N):
    original_labs.append(list(map(lambda x: int(x), input().split())))


def spread(labs):
    queue = deque()
    ancient = [[False for j in range(M)] for i in range(N)]

    for i in range(N):
        for j in range(M):
            if labs[i][j] == 2:
                ancient[i][j] = True
                queue.append((i, j))
    while len(queue) != 0:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not ancient[nx][ny] and labs[nx][ny] == 0:
                labs[nx][ny] = 2
                ancient[nx][ny] = True
                queue.append((nx, ny))

    safety = 0
    for i in range(N):
        for j in range(M):
            if labs[i][j] == 0:
                safety += 1
    return safety


def func(wall, flag):
    if wall < 3:
        for i in range(N):
            for j in range(M):
                if i*M + j <= flag:
                    continue
                if original_labs[i][j] == 0:
                    original_labs[i][j] = 1
                    func(wall+1, i*M + j)
                    original_labs[i][j] = 0
                # original_labs[i][j]
    else:
        global max_safety

        safety = spread(deepcopy(original_labs))
        if max_safety < safety:
            max_safety = safety




func(0, -1)
print(max_safety)
