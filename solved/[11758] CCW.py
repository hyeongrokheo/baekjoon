"""
problem tier : Gold 5 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

P = []
for i in range(3):
    P.append(list(map(int, input().split())))
P.append(P[0])

CCW = 0
for i in range(3):
    CCW += P[i][0] * P[i+1][1]
    CCW -= P[i+1][0] * P[i][1]

if CCW < 0:
    print(-1)
elif CCW == 0:
    print(0)
else:
    print(1)
