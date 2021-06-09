"""
problem tier : Gold 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())

points = []
for i in range(N):
    points.append(list(map(int, input().split())))

points.sort(key=lambda x: (x[0], -x[1]))

length = 0
s, e = -1000000000, -1000000000
for p in points:
    if p[0] > e:
        length += e-s
        s, e = p[0], p[1]
    else:
        e = max(e, p[1])

length += e-s
print(length)
