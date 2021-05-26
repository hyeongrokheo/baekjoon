"""
problem tier : Silver 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

max_weight = 0
ropes = []

for i in range(N):
    ropes.append(int(sys.stdin.readline()))
ropes.sort()

for i in range(N):
    if max_weight < ropes[i] * (N - i):
        max_weight = ropes[i] * (N - i)
print(max_weight)
