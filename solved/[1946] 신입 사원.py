"""
problem tier : Silver 1 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

while T:
    T -= 1

    N = int(input())

    appl = []
    for i in range(N):
        appl.append(list(map(int, sys.stdin.readline().split())))
    appl.sort(key=lambda x: x[0])

    count = 0
    max_score = 999999
    for i in range(N):
        if max_score > appl[i][1]:
            count += 1
            max_score = appl[i][1]

    print(count)

