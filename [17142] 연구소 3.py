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

def spread_virus(board, virus):
    x, y = virus








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
            if board[i][j] == 0:
                space_count += 1
            if board[i][j] == 2:
                virus_list.append((i, j))

    find_comb([], virus_list, M, [False for _ in range(len(virus_list))], 0)
    print(combinations)

    min_time = 9999
    for combination in combinations:
        virus_time = spread_virus(deepcopy(board), combination, space_count)
        if min_time > virus_time:
            min_time = virus_time

    print(min_time)



solution()
