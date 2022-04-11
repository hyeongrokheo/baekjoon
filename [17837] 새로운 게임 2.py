"""
problem tier : Gold 2 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')


# 오른 왼 위 아래
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def move_tokens(board, tokens, directions, token_positions)


def solution():
    N, K = map(int, input().split())
    board = []
    tokens = [[[] for _ in range(N)] for _ in range(N)]
    directions = []
    token_positions = []

    for _ in range(N):
        board.append(list(map(int, input().split())))
    for k in range(K):
        r, c, d = map(lambda x: int(x)-1, input().split())
        tokens[r][c].append(k)
        directions.append(d)
        token_positions.append([r, c])

    for b in board:
        print(b)

    for t in tokens:
        print(t)

    print(directions)

    print(token_positions)

    count = 0
    while count < 1001:
        move_tokens(board, tokens, directions, token_positions)
        count += 1




solution()
