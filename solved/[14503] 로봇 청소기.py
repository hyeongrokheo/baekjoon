"""
problem tier : Gold 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def left_dir(d):
    return (d + 3) % 4


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []
clean_count = 0

def clean(x, y, d):
    global clean_count
    if board[x][y] == 0:
        board[x][y] = 2
        clean_count += 1

    for i in range(4):
        d = left_dir(d)
        new_x = x + dx[d]
        new_y = y + dy[d]
        if board[new_x][new_y] == 0:
            clean(new_x, new_y, d)
            return

    new_x = x - dx[d]
    new_y = y - dy[d]
    if board[new_x][new_y] != 1:
        clean(new_x, new_y, d)
    else:
        return


def solution():
    global board
    N, M = map(int, input().split())
    x, y, d = map(int, input().split())
    for i in range(N):
        board.append(list(map(int, input().split())))

    clean(x, y, d)
    print(clean_count)


solution()
