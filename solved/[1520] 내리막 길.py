"""
problem tier : Gold 4 (solved.ac)
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

memo = [[-1 for j in range(M)] for i in range(N)]
memo[0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def search(x, y):
    if memo[x][y] != -1:
        return memo[x][y]
    result = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] > maps[x][y]:
            result += search(nx, ny)
    memo[x][y] = result
    return memo[x][y]

print(search(N-1, M-1))
