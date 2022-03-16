"""
problem tier : Gold 2 (solved.ac)
"""

from copy import deepcopy
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def rotate(original):
    rotated = deepcopy(original)
    for i in range(N):
        for j in range(N):
            rotated[j][N-1-i] = original[i][j]
    return rotated


max_num = 0
N = None


def move_left_line(line):
    new_line = []
    merge_flag = False
    for e in line:
        if e == 0:
            None
        elif len(new_line) == 0:
            new_line.append(e)
        else:
            if new_line[-1] == e:
                if not merge_flag:
                    new_line[-1] = 2 * e
                    merge_flag = True
                else:
                    new_line.append(e)
                    merge_flag = False
            else:
                new_line.append(e)
                merge_flag = False
    while len(new_line) < len(line):
        new_line.append(0)
    return new_line


def DFS(board, depth):
    global max_num
    if depth == 5:
        for line in board:
            if max_num < max(line):
                max_num = max(line)
    else:
        for i in range(4):
            next_board = deepcopy(board)
            for i in range(N):
                next_board[i] = move_left_line(next_board[i])

            DFS(next_board, depth+1)
            board = rotate(board)


def solution():
    global N
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    DFS(board, 0)
    print(max_num)


solution()
