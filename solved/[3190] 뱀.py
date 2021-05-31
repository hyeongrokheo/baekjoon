"""
problem tier : Gold 5 (solved.ac)
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

maps = [[0 for j in range(N)] for i in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    maps[x-1][y-1] = 1

L = int(input())
moves = deque()
for i in range(L):
    inp = input().split()
    T = int(inp[0])
    D = inp[1]
    moves.append([T, D])
time = 0
next_move = moves.popleft()
d = [[0, 1], [-1, 0], [0, -1], [1, 0]]
direction = 0
x = 0
y = 0
maps[0][0] = 2

snake = deque()
snake.append([0, 0])

while True:
    time += 1
    nx, ny = x + d[direction][0], y + d[direction][1]
    if not (0 <= nx < N and 0 <= ny < N):
        print(time)
        break
    if maps[nx][ny] == 0:
        snake.append([nx, ny])
        maps[nx][ny] = 2
        tail = snake.popleft()
        maps[tail[0]][tail[1]] = 0
    elif maps[nx][ny] == 1:
        snake.append([nx, ny])
        maps[nx][ny] = 2
    else:
        print(time)
        break

    if next_move[0] == time:
        if next_move[1] == 'L':
            direction += 1
        else:
            direction -= 1

        if direction < 0:
            direction += 4
        if direction > 3:
            direction -= 4

        if len(moves) != 0:
            next_move = moves.popleft()
        else:
            next_move = [99999, '?']

    x, y = nx, ny
