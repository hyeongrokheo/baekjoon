"""
problem tier : Gold 5 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

S = []
for i in range(N):
    n = num[i]
    while True:
        if len(S) != 0 and S[-1][0] < n:
            S.pop()
        else:
            if len(S) == 0:
                print(0)
            else:
                print(S[-1][1])
            S.append([n, i+1])
            break