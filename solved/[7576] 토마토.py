"""
problem tier : Silver 1 (solved_old.ac)
"""

from collections import deque
M, N = map(lambda x: int(x), input().split())

tomatoes = []
for i in range(N):
    tomatoes.append(list(map(lambda x: int(x), input().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append([i, j, 0])

day = 0
while len(queue) > 0:
    tomato = queue.popleft()
    x, y = tomato[0], tomato[1]
    day = tomato[2]
    if x+1 < N and tomatoes[x+1][y] == 0:
        tomatoes[x+1][y] = 1
        queue.append([x+1, y, tomato[2]+1])
    if x-1 >= 0 and tomatoes[x-1][y] == 0:
        tomatoes[x-1][y] = 1
        queue.append([x-1, y, tomato[2]+1])
    if y+1 < M and tomatoes[x][y+1] == 0:
        tomatoes[x][y+1] = 1
        queue.append([x, y+1, tomato[2]+1])
    if y-1 >= 0 and tomatoes[x][y-1] == 0:
        tomatoes[x][y-1] = 1
        queue.append([x, y-1, tomato[2]+1])

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            print(-1)
            exit()

print(day)
