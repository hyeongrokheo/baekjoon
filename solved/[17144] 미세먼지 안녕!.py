"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution():
    R, C, T = map(int, input().split())
    board = []
    for _ in range(R):
        board.append(list(map(int, input().split())))

    AC = []
    for i in range(R):
        # for j in range(C):
        if board[i][0] == -1:
            AC.append((i, 0))

    for _ in range(T):
        spread_board = [[0 for j in range(C)] for i in range(R)]

        for r in range(R):
            for c in range(C):
                if board[r][c] < 5:
                    continue
                spread = board[r][c] // 5
                for d in range(4):
                    new_r = r + dx[d]
                    new_c = c + dy[d]
                    if not (0 <= new_r < R and 0 <= new_c < C):
                        continue
                    if board[new_r][new_c] == -1:
                        continue
                    spread_board[r][c] -= spread
                    spread_board[new_r][new_c] += spread

        for r in range(R):
            for c in range(C):
                board[r][c] += spread_board[r][c]

        origin_r, origin_c = AC[0]
        r, c = origin_r, origin_c
        dust = 0
        for d in [1, 2, 3, 0]:
            while True:
                new_r = r + dx[d]
                new_c = c + dy[d]
                if not (0 <= new_r < R and 0 <= new_c < C):
                    break
                if board[new_r][new_c] == -1:
                    break

                next_dust = board[new_r][new_c]
                board[new_r][new_c] = dust
                dust = next_dust
                r, c = new_r, new_c

        origin_r, origin_c = AC[1]
        r, c = origin_r, origin_c
        dust = 0
        for d in [1, 0, 3, 2]:
            while True:
                new_r = r + dx[d]
                new_c = c + dy[d]
                if not (0 <= new_r < R and 0 <= new_c < C):
                    break
                if board[new_r][new_c] == -1:
                    break

                next_dust = board[new_r][new_c]
                board[new_r][new_c] = dust
                dust = next_dust
                r, c = new_r, new_c

    result = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == -1:
                continue
            result += board[r][c]

    print(result)


solution()
