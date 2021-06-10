"""
problem tier : Platinum 3 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))

points.sort()
