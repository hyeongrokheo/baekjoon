"""
problem tier : Silver 1 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
N = None
M = None
board = None


def DFS(x, y, S):
    if 0 <= x < N and 0 <= y < M and board[x][y] == False:
        board[x][y] = True
        S += 1
        for i in range(4):
            S += DFS(x + dx[i], y + dy[i], 0)
    return S


def solution():
    global N
    global M
    global board
    M, N, K = map(int, input().split())
    # print(M, N, K)
    board = [[False for j in range(M)] for i in range(N)]
    # for b in board:
    #     print(b)

    for i in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(x1, x2):
            for k in range(y1, y2):
                board[j][k] = True


    # print()
    # for b in board:
    #     print(b)
    count = 0
    S_list = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == False:
                # for b in board:
                #     print(list(map(lambda x: 'X' if x == True else ' ', b)))
                # print(i, j)
                S_list.append(DFS(i, j, 0))
                count += 1
    # return count
    print(count)
    S_list.sort()
    print(' '.join(list(map(str, S_list))))

solution()
