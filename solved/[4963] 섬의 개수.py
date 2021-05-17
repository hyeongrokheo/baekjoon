"""
problem tier : Silver 2 (solved_old.ac)
"""

import sys
sys.setrecursionlimit(10**8)

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

def search(i, j):
    # print(i, j, S)
    S[i][j] = 0
    for k in range(8):
        x = i+dx[k]
        y = j+dy[k]
        if 0 <= x < h and 0 <= y < w and S[x][y] == 1:
            search(x, y)

while True:
    w, h = map(lambda x: int(x), input().split())
    if w == 0 and h == 0:
        break

    S = []
    for i in range(h):
        S.append(list(map(lambda x: int(x), input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if S[i][j] == 1:
                search(i, j)
                # print(S)
                count += 1
    print(count)
