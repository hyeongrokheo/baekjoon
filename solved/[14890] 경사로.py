"""
problem tier : Gold 3 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


def rotated(original):
    rotated_board = [[] for i in range(N)]

    for i in range(N):
        for j in range(N):
            rotated_board[i].append(original[j][i])

    return rotated_board


def can_move(line, L):
    previous = line[0]
    count = 0
    need_L = False
    for l in line:
        if l == previous:
            count += 1
        else:
            if need_L:
                return False
            if l == previous + 1:
                if count >= L:
                    count = 1
                else:
                    return False
            elif l == previous - 1:
                need_L = True
                count = 1
            else:
                return False

        if need_L and count == L:
            need_L = False
            count = 0

        previous = l

    if need_L:
        return False
    else:
        return True


def solution():
    global N
    N, L = map(int, input().split())

    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    board.extend(rotated(board))

    count = 0
    for i in range(N * 2):
        if can_move(board[i], L):
            count += 1

    print(count)


solution()
