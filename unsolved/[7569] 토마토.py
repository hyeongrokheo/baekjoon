"""
problem tier : Silver 1 (solved_old.ac)
"""

from collections import deque
M, N, H = map(lambda x: int(x), input().split())

tomatoes = []
for j in range(H):
    box = []
    for i in range(N):
        box.append(list(map(lambda x: int(x), input().split())))
    tomatoes.append(box)

# print(tomatoes)
# exit()

queue = deque()
for i in range(N):
    for j in range(M):
        for k in range(H):
            if tomatoes[k][i][j] == 1:
                queue.append([i, j, k, 0])

day = 0
while len(queue) > 0:
    tomato = queue.popleft()
    x, y, z = tomato[0], tomato[1], tomato[2]
    day = tomato[3]
    if x+1 < N and tomatoes[z][x+1][y] == 0:
        tomatoes[z][x+1][y] = 1
        queue.append([x+1, y, z, day+1])
    if x-1 >= 0 and tomatoes[z][x-1][y] == 0:
        tomatoes[z][x-1][y] = 1
        queue.append([x-1, y, z, day+1])
    if y+1 < M and tomatoes[z][x][y+1] == 0:
        tomatoes[z][x][y+1] = 1
        queue.append([x, y+1, z, day+1])
    if y-1 >= 0 and tomatoes[z][x][y-1] == 0:
        tomatoes[z][x][y-1] = 1
        queue.append([x, y-1, z, day+1])
    if z+1 < H and tomatoes[z+1][x][y] == 0:
        tomatoes[z+1][x][y] = 1
        queue.append([x, y, z+1, day+1])
    if z-1 >= 0 and tomatoes[z-1][x][y] == 0:
        tomatoes[z-1][x][y] = 1
        queue.append([x, y, z-1, day+1])

for i in range(N):
    for j in range(M):
        for k in range(H):
            if tomatoes[k][i][j] == 0:
                print(-1)
                exit()

print(day)
