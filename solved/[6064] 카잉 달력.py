"""
problem tier : Silver 1 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

T = int(input())

while T:
    T -= 1
    M, N, x, y = map(int, input().split())

    day = x
    while True:
        if day > M * N:
            print(-1)
            break
        # print('day :', day)
        if day % N == y or (day-1) % N + 1 == y:
            print(day)
            break
        day += M
