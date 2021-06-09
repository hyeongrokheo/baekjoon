"""
problem tier : Gold 3 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

points = []
for i in range(N):
    s, e = map(int, input().split())
    if s > e:
        points.append([e, s])

points.sort(key=lambda x: x[0])

length = 0
s, e = 0, 0
for p in points:
    if p[0] > e:
        length += e-s
        s, e = p[0], p[1]
    else:
        e = max(e, p[1])

length += e-s

print(M + length*2)
