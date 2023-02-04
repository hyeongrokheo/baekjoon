"""
problem tier : Silver 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')


def solution():
    N, M = map(int, input().split())
    square = [list(map(int, list(input()))) for _ in range(N)]

    size = min(N, M)
    while size > 1:
        width = size-1
        for x in range(N):
            for y in range(M):
                if x+width >= N or y+width >= M:
                    continue
                points = [square[x][y], square[x+width][y], square[x][y+width], square[x+width][y+width]]
                if len(set(points)) == 1:
                    print(size * size)
                    return
        size -= 1
    print(1)


solution()
