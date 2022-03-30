"""
problem tier : Gold 4 (solved.ac)
"""

from collections import deque
from copy import deepcopy
import sys
sys.stdin = open('./input.txt', 'r')

combinations = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def find_comb(current_comb, virus_list, M, visited, flag):
    global combinations
    if len(current_comb) == M:
        combinations.append(deepcopy(current_comb))
    else:
        for i in range(flag, len(virus_list)):
            if visited[i]:
                continue
            current_comb.append(virus_list[i])
            visited[i] = True
            find_comb(current_comb, virus_list, M, visited, i+1)
            current_comb.pop()
            visited[i] = False


def spread_virus(N, board, virus_list, space_count):
    visited = [[False for _ in range(N)] for _ in range(N)]
    Q = deque()
    max_t = 0

    for virus in virus_list:
        x, y = virus
        Q.append((x, y, 0))
    while len(Q):
        x, y, t = Q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True

        if board[x][y] == 1:
            continue
        elif board[x][y] == 0:
            if max_t < t:
                max_t = t

        board[x][y] = -1
        space_count -= 1

        for d in range(4):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if not (0 <= new_x < N and 0 <= new_y < N):
                continue
            Q.append((new_x, new_y, t+1))

    if space_count != 0:
        return 9999
    else:
        return max_t


def solution():
    global combinations
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    virus_list = []
    space_count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 1:
                # print(i, j)
                space_count += 1
            if board[i][j] == 2:
                virus_list.append((i, j))

    find_comb([], virus_list, M, [False for _ in range(len(virus_list))], 0)

    min_time = 9999
    for combination in combinations:
        virus_time = spread_virus(N, deepcopy(board), combination, space_count)
        if min_time > virus_time:
            min_time = virus_time

    if min_time == 9999:
        print(-1)
    else:
        print(min_time)


solution()
