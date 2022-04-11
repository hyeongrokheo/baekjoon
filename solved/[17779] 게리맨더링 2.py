"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')


def do_elec(N, board, x, y, d1, d2):
    new_board = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if 0 <= r < x + d1 and 0 <= c <= y:
                new_board[r][c] = 1
            elif 0 <= r <= x + d2 and y < c < N:
                new_board[r][c] = 2
            elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                new_board[r][c] = 3
            elif x + d2 < r < N and y - d1 + d2 <= c < N:
                new_board[r][c] = 4

    r, left, right = x, y, y+1

    for new_r in range(r, N):
        for new_c in range(left, right):
            new_board[new_r][new_c] = 5

        d1 -= 1
        d2 -= 1
        if d1 >= 0:
            left -= 1
        else:
            left += 1

        if d2 >= 0:
            right += 1
        else:
            right -= 1

    elec_result = [0, 0, 0, 0, 0]
    for r in range(N):
        for c in range(N):
            elec_result[new_board[r][c] - 1] += board[r][c]
    return max(elec_result) - min(elec_result)


def solution():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    min_score = 999999
    for x in range(N):
        for y in range(N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if not (x + d1 + d2 < N):
                        continue
                    if not (0 < y-d1 < y < y+d2 < N):
                        continue
                    score = do_elec(N, board, x, y, d1, d2)
                    if min_score > score:
                        min_score = score

    print(min_score)


solution()
