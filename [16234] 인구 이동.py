"""
problem tier : Gold 5 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')
from collections import deque


population = []
N, L, R = None, None, None
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
migration_count = 0


def get_group(i, j, visited, borders):
    group = [(i, j)]
    Q = deque()
    Q.append((i, j))

    while len(Q) != 0:
        x, y = Q.popleft()

        for d in range(4):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if not (0 <= new_x < N and 0 <= new_y < N):
                continue

            if visited[new_x][new_y]:
                continue

            if borders[x * N + y][new_x * N + new_y]:
                visited[new_x][new_y] = True
                Q.append((new_x, new_y))
                group.append((new_x, new_y))

    return group


def get_border():

    borders = [[False for j in range(N * N)] for i in range(N * N)]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                new_i = i + dx[d]
                new_j = j + dy[d]
                if 0 <= new_i < N and 0 <= new_j < N:
                    if L <= abs(population[i][j] - population[new_i][new_j]) <= R:
                        borders[i * N + j][new_i * N + new_j] = True
                        borders[new_i * N + new_j][i * N + j] = True

    return borders


def migration():
    global migration_count
    borders = get_border()
    visited = [[False for j in range(N)] for i in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            else:
                visited[i][j] = True
                group = get_group(i, j, visited, borders)
                if len(group) > 1:
                    groups.append(group)
    if len(groups) > 0:
        migration_count += 1
    else:
        return False

    for group in groups:
        P = 0
        for x, y in group:
            P += population[x][y]
        P = P // len(group)
        for x, y in group:
            population[x][y] = P

    return True


def solution():
    global population
    global N, L, R

    N, L, R = map(int, input().split())
    for i in range(N):
        population.append(list(map(int, input().split())))

    while True:
        migration_result = migration()
        if not migration_result:
            break

    print(migration_count)

solution()
