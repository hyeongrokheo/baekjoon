"""
problem tier : Gold 3 (solved.ac)
"""

import sys
from collections import deque
sys.stdin = open('../input.txt', 'r')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def get_target_fish(N, board, shark_x, shark_y, shark_size):
    fish_list = []
    min_dist = 9999
    visited = [[False for j in range(N)] for i in range(N)]

    Q = deque()
    Q.append((shark_x, shark_y, 0))

    while len(Q):
        x, y, dist = Q.popleft()

        if min_dist < dist:
            continue
        if visited[x][y]:
            continue
        visited[x][y] = True
        if board[x][y] > shark_size:
            continue

        if board[x][y] != 0 and board[x][y] != shark_size:
            if min_dist >= dist:
                fish_list.append((x, y, dist))
                min_dist = dist

        for d in range(4):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if not (0 <= new_x < N and 0 <= new_y < N):
                continue
            Q.append((new_x, new_y, dist+1))

    if len(fish_list) == 0:
        return -1, -1, -1
    elif len(fish_list) == 1:
        return fish_list[0]
    else:
        fish_list.sort(key=lambda x: (x[0], x[1]))
        return fish_list[0]


def solution():
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                shark_x = i
                shark_y = j
                board[i][j] = 0

    shark_size = 2
    shark_feed = 0
    current_time = 0

    while True:
        target_x, target_y, dist = get_target_fish(N, board, shark_x, shark_y, shark_size)
        if (target_x, target_y) == (-1, -1):
            break
        shark_x, shark_y = target_x, target_y
        board[target_x][target_y] = 0
        current_time += dist
        shark_feed += 1
        if shark_size == shark_feed:
            shark_size += 1
            shark_feed = 0

    print(current_time)


solution()
