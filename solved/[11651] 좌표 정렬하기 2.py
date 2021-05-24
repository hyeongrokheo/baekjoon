"""
problem tier : Silver 5 (solved.ac)
"""

import sys

N = int(input())
arr = []
for i in range(N):
    X, Y = map(lambda x: int(x), sys.stdin.readline().strip().split())
    arr.append([X, Y])

arr.sort(key=lambda x: (x[1], x[0]))

for X, Y in arr:
    print(X, Y)
