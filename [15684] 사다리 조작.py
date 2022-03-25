"""
problem tier : Gold 4 (solved.ac)
"""

import sys

sys.stdin = open('./input.txt', 'r')

N, M, H = None, None, None
find_flag = False


def check_ladders(ladders):
    for i in range(N):
        position = i

        for h in range(H):
            if position >= 1 and ladders[h][position - 1]:
                position -= 1
            elif position < N-1 and ladders[h][position]:
                position += 1

        if position != i:
            return False
    return True


def DFS(ladders, depth, target_depth, x, y):
    global find_flag

    if check_ladders(ladders):
        print(depth)
        exit()
        find_flag = True
    else:
        if depth < target_depth:
            for i in range(x, H):
                for j in range(y, N-1):
                    if ladders[i][j]:
                        continue
                    elif j != 0 and ladders[i][j-1]:
                        continue
                    elif j != N-2 and ladders[i][j+1]:
                        continue
                    else:
                        ladders[i][j] = True
                        DFS(ladders, depth+1, target_depth, i, j)
                        ladders[i][j] = False
                y = 0


def solution():
    global N, M, H
    global find_flag
    N, M, H = map(int, input().split())

    ladders = [[False for i in range(N-1)] for j in range(H)]
    for i in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        ladders[a][b] = True

    target_depth = 0
    while True:
        DFS(ladders, 0, target_depth, 0, 0)
        # if find_flag:
        #     print(target_depth)
        #     break
        if target_depth == 3:
            print(-1)
            break
        target_depth += 1


solution()
