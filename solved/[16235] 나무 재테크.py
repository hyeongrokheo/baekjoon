"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring_summer(N, trees, foods):
    for x in range(N):
        for y in range(N):
            death_tree_energy = 0
            tree = trees[x][y]
            new_tree = deque()
            while len(tree):
                t = tree.popleft()
                if foods[x][y] >= t:
                    foods[x][y] -= t
                    new_tree.append(t+1)
                else:
                    death_tree_energy += t // 2
            trees[x][y] = new_tree
            foods[x][y] += death_tree_energy


def fall(N, trees):
    for x in range(N):
        for y in range(N):
            for tree in trees[x][y]:
                if tree % 5 == 0:
                    for d in range(8):
                        new_x = x + dx[d]
                        new_y = y + dy[d]
                        if 0 <= new_x < N and 0 <= new_y < N:
                            trees[new_x][new_y].appendleft(1)


def winter(N, foods, A):
    for x in range(N):
        for y in range(N):
            foods[x][y] += A[x][y]


def solution():
    N, M, K = map(int, input().split())
    trees = [[[] for j in range(N)] for i in range(N)]
    foods = [[5 for j in range(N)] for i in range(N)]
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    for _ in range(M):
        x, y, z = map(int, input().split())
        trees[x-1][y-1].append(z)

    for x in range(N):
        for y in range(N):
            trees[x][y] = deque(sorted(trees[x][y]))

    for _ in range(K):
        spring_summer(N, trees, foods)
        fall(N, trees)
        winter(N, foods, A)

    result = 0
    for x in range(N):
        for y in range(N):
            result += len(trees[x][y])

    print(result)


solution()
