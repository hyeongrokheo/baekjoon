"""
problem tier : Silver 5 (solved_old.ac)
"""

import sys


N = int(input())

arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for n in arr:
    print(n)
