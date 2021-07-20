"""
problem tier : Gold 2 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

dx_list = [1, -1, 0, 0]
dy_list = [0, 0, 1, -1]

def move(board, depth):
    if depth == 1:
        max_num = 0
        for i in range(N):
            for j in range(N):
                if max_num < board[i][j]:
                    max_num = board[i][j]
        return max_num
    else:
        for i in range(4):
            dx, dy = dx_list[i], dy_list[i]
            



print(move(board, 0))
