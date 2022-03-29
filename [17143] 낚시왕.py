"""
problem tier : Gold 2 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def get_shark(board, R, i):
    shark_size = 0
    for r in range(R):
        if board[r][i]:
            shark_size = board[r][i][2]
            board[r][i] = None
            break
    return shark_size


def move_shark(board, R, C):
    moved = [[None for j in range(C)] for i in range(R)]
    for r in range(R):
        for c in range(C):
            if not board[r][c]:
                continue
            s = board[r][c][0]
            d = board[r][c][1]
            new_r, new_c = r, c
            while s:
                if 0 <= new_r + dr[d] < R and 0 <= new_c + dc[d] < C:
                    new_r = new_r + dr[d]
                    new_c = new_c + dc[d]
                    s -= 1
                else:
                    if d == 0:
                        d = 1
                        board[r][c][1] = 1
                    elif d == 1:
                        d = 0
                        board[r][c][1] = 0
                    elif d == 2:
                        d = 3
                        board[r][c][1] = 3
                    else:
                        d = 2
                        board[r][c][1] = 2
            if moved[new_r][new_c]:
                moved[new_r][new_c] = max(moved[new_r][new_c], board[r][c], key=lambda x: x[2])
            else:
                moved[new_r][new_c] = board[r][c]

    return moved


def solution():
    R, C, M = map(int, input().split())

    board = [[None for j in range(C)] for i in range(R)]
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        board[r-1][c-1] = [s, d-1, z]

    size_sum = 0

    # for b in board:
    #     print(b)
    # print()

    for fisher in range(C):
        shark_size = get_shark(board, R, fisher)
        # print('get shark', shark_size)
        board = move_shark(board, R, C)
        size_sum += shark_size
        # for b in board:
        #     print(b)
        # print()

    print(size_sum)



solution()
