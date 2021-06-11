"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())

points = list(map(lambda x: [int(x), int(x)], input().split()))
for i in range(N-1):
    a, b, c = map(int, input().split())
    points = [[max(points[0][0], points[1][0]) + a, min(points[0][1], points[1][1]) + a],
              [max(points[0][0], points[1][0], points[2][0]) + b, min(points[0][1], points[1][1], points[2][1]) + b],
              [max(points[1][0], points[2][0]) + c, min(points[1][1], points[2][1]) + c]]

print(max(list(map(lambda x: x[0], points))), min(list(map(lambda x: x[1], points))))
