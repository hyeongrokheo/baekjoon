"""
problem tier : Gold 3 (solved.ac)
"""
# 1557 - 1716

import sys
sys.stdin = open('./input.txt', 'r')
from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def get_target_fish(N, board, shark_x, shark_y, shark_size):
    fish_list = []
    min_dist = 99
    visited = [[False for j in range(N)] for i in range(N)]

    Q = deque()
    Q.append((shark_x, shark_y, 0))

    while len(Q):
        x, y, dist = Q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        if board[x][y] > shark_size:
            continue
        if board[x][y] != 0 and board[x][y] != shark_size:
            if min_dist > dist:
                fish_list.append((x, y, dist))
                min_dist = dist
            # elif min_dist < dist:
            #     None


        for d in range(4):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if not (0 <= new_x < N and 0 <= new_y < N):
                continue
            # if visited[new_x][new_y] = True
            # if board[new_x][new_y] > shark_size:
            #     continue
            # if shark_size >= board[new_x][new_y]:
            Q.append((new_x, new_y, dist+1))

    print(fish_list)
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
        print(shark_x, shark_y, shark_size, current_time)
        print(target_x, target_y, dist)
        if (target_x, target_y) == (-1, -1):
            break
        # fish_size = board[target_x][target_y]
        shark_x, shark_y = target_x, target_y
        board[target_x][target_y] = 0
        current_time += dist
        # if fish_size == shark_size:
        shark_feed += 1
        if shark_size == shark_feed:
            shark_size += 1
            shark_feed = 0

    print(current_time)


solution()
