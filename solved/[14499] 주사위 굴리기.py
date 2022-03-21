"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def move_dice(dice, dir):
    if dir == 1:  # 동
        dice = [dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]]
    elif dir == 2:  # 서
        dice = [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]
    elif dir == 3:  # 북
        dice = [dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]]
    else:  # 남
        dice = [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]

    return dice


def solution():
    N, M, x, y, K = map(int, input().split())
    # print(N, M, x, y, K)
    board = []
    dice = [0, 0, 0, 0, 0, 0]  # 0 top, 1 up, 2 right, 3 down, 4 left, 5 bottom
    for i in range(N):
        board.append(list(map(int, input().split())))

    commands = list(map(int, input().split()))
    for c in commands:
        # print('command :', c)
        if c == 1:  # 동
            if 0 <= y+1 < M:
                y = y+1
                dice = move_dice(dice, c)
                if board[x][y] == 0:
                    board[x][y] = dice[5]
                else:
                    dice[5] = board[x][y]
                    board[x][y] = 0
                print(dice[0])
        elif c == 2:  # 서
            if 0 <= y-1 < M:
                y = y-1
                dice = move_dice(dice, c)
                if board[x][y] == 0:
                    board[x][y] = dice[5]
                else:
                    dice[5] = board[x][y]
                    board[x][y] = 0
                print(dice[0])
        elif c == 3:  # 북
            if 0 <= x-1 < N:
                x = x-1
                dice = move_dice(dice, c)
                if board[x][y] == 0:
                    board[x][y] = dice[5]
                else:
                    dice[5] = board[x][y]
                    board[x][y] = 0
                print(dice[0])
        else:  # 남
            if 0 <= x+1 < N:
                x = x+1
                dice = move_dice(dice, c)
                if board[x][y] == 0:
                    board[x][y] = dice[5]
                else:
                    dice[5] = board[x][y]
                    board[x][y] = 0
                print(dice[0])
        # print('dice :', dice)
        # print('position :', x, y)


solution()
