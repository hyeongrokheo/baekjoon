"""
problem tier : Silver 2 (solved.ac)
"""


import sys
sys.setrecursionlimit(100000)

T = int(input())
field = None


def worm(X, Y):
    if X < 0 or Y < 0:
        return
    if X >= M or Y >= N:
        return
    if field[X][Y] == 1:
        field[X][Y] = 2
        worm(X, Y+1)
        worm(X, Y-1)
        worm(X+1, Y)
        worm(X-1, Y)
        return 1
    return 0


while T:
    T -= 1

    M, N, K = map(lambda x: int(x), input().split())
    field = [[0 for i in range(N)] for j in range(M)]
    for i in range(K):
        X, Y = map(lambda x: int(x), input().split())
        field[X][Y] = 1
    earthworm = 0

    for i in range(M):
        for j in range(N):
            earthworm += worm(i, j)
    print(earthworm)
