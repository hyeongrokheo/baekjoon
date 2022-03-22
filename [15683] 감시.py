"""
problem tier : Gold 3 (solved.ac)
"""

# 70분

from copy import deepcopy
import sys
sys.stdin = open('./input.txt', 'r')

original_office = []
N, M = None, None

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_direction_list = []
min_count = 100

def mask_line(office, x, y, direction):
    while True:
        x += dx[direction]
        y += dy[direction]
        if not (0 <= x < N and 0 <= y < M):
            break
        if office[x][y] == 6:
            break
        elif office[x][y] == 0:
            office[x][y] = -1



def mask_space(office, original_x, original_y, camera_direction):
    camera_type = office[original_x][original_y]
    if camera_type == 1:
        mask_line(office, original_x, original_y, camera_direction)
    elif camera_type == 2:
        mask_line(office, original_x, original_y, camera_direction)
        mask_line(office, original_x, original_y, (camera_direction + 2) % 4)
    elif camera_type == 3:
        mask_line(office, original_x, original_y, camera_direction)
        mask_line(office, original_x, original_y, (camera_direction + 1) % 4)
    elif camera_type == 4:
        mask_line(office, original_x, original_y, camera_direction)
        mask_line(office, original_x, original_y, (camera_direction + 1) % 4)
        mask_line(office, original_x, original_y, (camera_direction + 2) % 4)
    elif camera_type == 5:
        mask_line(office, original_x, original_y, camera_direction)
        mask_line(office, original_x, original_y, (camera_direction + 1) % 4)
        mask_line(office, original_x, original_y, (camera_direction + 2) % 4)
        mask_line(office, original_x, original_y, (camera_direction + 3) % 4)


def search_space(original_camera_direction_list):
    global min_count
    office = deepcopy(original_office)
    camera_direction_list = deepcopy(original_camera_direction_list)

    for i in range(N):
        for j in range(M):
            if 1 <= office[i][j] <= 5:
                mask_space(office, i, j, camera_direction_list.pop(0))

    count = 0
    for i in range(N):
        for j in range(M):
            if office[i][j] == 0:
                count += 1
    if min_count > count:
        min_count = count

def DFS(camera_direction_list):

    if len(camera_direction_list) == len(max_direction_list):
        search_space(camera_direction_list)

    elif len(camera_direction_list) < len(max_direction_list):
        for i in range(max_direction_list[len(camera_direction_list)]):
            camera_direction_list.append(i)
            DFS(camera_direction_list)
            camera_direction_list.pop()


def solution():
    global original_office, N, M
    global max_direction_list
    N, M = map(int, input().split())
    for i in range(N):
        original_office.append(list(map(int, input().split())))


    for i in range(N):
        for j in range(M):
            if original_office[i][j] in [1, 3, 4]:
                max_direction_list.append(4)
            elif original_office[i][j] == 2:
                max_direction_list.append(2)
            elif original_office[i][j] == 5:
                max_direction_list.append(1)

    DFS([])

    print(min_count)


solution()
