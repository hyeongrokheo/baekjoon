"""
problem tier : Gold 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())

maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#     북 동 남 서

clear_count = 0

while True:
    if maps[x][y] == 0:
        maps[x][y] = 2
        clear_count += 1
    all_cleared = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 0:
            all_cleared = False

    if all_cleared:  # 네 방향 모두 청소가 이미 되어있으면
        nd = (d+2) % 4
        nx, ny = x + dx[nd], y + dy[nd]

        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] != 1:  # 뒤가 벽이 아님
            x, y = nx, ny
            continue
        else:  # 뒤가 벽임
            break

    d = (d-1) % 4
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 0:
        x, y = nx, ny
    else:
        None

print(clear_count)
