"""
problem tier : Gold 3 (solved.ac)
"""

# 50분

from copy import deepcopy
import sys
sys.stdin = open('../input.txt', 'r')

original_office = []
N, M = None, None

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def mask_space(office, original_x, original_y, camera_direction):
    camera_type = office[original_x][original_y]
    # original_x, original_y = x, y

    if camera_type == 1:
        x, y = original_x, original_y
        while True:
            x += dx[camera_direction]
            y += dy[camera_direction]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
    elif camera_type == 2:
        x, y = original_x, original_y
        while True:
            x += dx[camera_direction]
            y += dy[camera_direction]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
        x, y = original_x, original_y
        while True:
            x += dx[(camera_direction + 2) % 4]
            y += dy[(camera_direction + 2) % 4]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
    elif camera_type == 3:
        x, y = original_x, original_y
        while True:
            x += dx[camera_direction]
            y += dy[camera_direction]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
        x, y = original_x, original_y
        while True:
            x += dx[(camera_direction + 1) % 4]
            y += dy[(camera_direction + 1) % 4]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
    elif camera_type == 4:
        x, y = original_x, original_y
        while True:
            x += dx[camera_direction]
            y += dy[camera_direction]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
        x, y = original_x, original_y
        while True:
            x += dx[(camera_direction + 1) % 4]
            y += dy[(camera_direction + 1) % 4]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
        x, y = original_x, original_y
        while True:
            x += dx[(camera_direction + 2) % 4]
            y += dy[(camera_direction + 2) % 4]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
    elif camera_type == 5:
        x, y = original_x, original_y
        while True:
            x += dx[camera_direction]
            y += dy[camera_direction]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
        x, y = original_x, original_y
        while True:
            x += dx[(camera_direction + 1) % 4]
            y += dy[(camera_direction + 1) % 4]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
        x, y = original_x, original_y
        while True:
            x += dx[(camera_direction + 2) % 4]
            y += dy[(camera_direction + 2) % 4]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break
        while True:
            x += dx[(camera_direction + 3) % 4]
            y += dy[(camera_direction + 3) % 4]
            if not (0 <= x < N and 0 <= y < M):
                break
            if office[x][y] != 6:
                office[x][y] = -1
            else:
                break


def search_space(camera_directions):
    office = deepcopy(original_office)

    for i in range(N):
        for j in range(N):
            if 1 <= office[i][j] <= 5:
                mask_space(office, i, j, camera_directions.pop(0))

    for o in office:
        print(o)


def solution():
    global original_office, N, M
    N, M = map(int, input().split())
    # office = []
    for i in range(N):
        original_office.append(list(map(int, input().split())))

    max_direction_list = []
    for i in range(N):
        for j in range(M):
            if original_office in [1, 3, 4]:
                max_direction_list.append(4)

    camera_direction_list = []

    search_space([])


solution()
